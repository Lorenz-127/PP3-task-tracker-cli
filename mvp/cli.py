from typing import List, Optional
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from simple_term_menu import TerminalMenu
from model import Todo
from google_sheets_db import TodoGoogleSheets
from datetime import datetime

console = Console()


class TodoCLI:
    def __init__(self):
        """
        Initialize the TodoCLI with menu items and Google Sheets integration.
        """
        self.menu_items = {
            "main": [
                "[1] Add Todo",
                "[2] Show Todo's",
                "[3] Update Todo",
                "[4] Complete Todo",
                "[5] Delete Todo",
                "[6] Show Statistics",
                "",
                "[q] Exit",
            ],
            "confirm": ["Yes", "No"],
        }
        self.gs = TodoGoogleSheets()

    def display_menu(self, menu_type: str, title: str) -> int:
        """
        Display a menu of the specified type and return the selected option.

        Args:
            menu_type (str): The type of menu to display.
            title (str): The title of the menu.

        Returns:
            int: The index of the selected menu item.
        """
        main_menu_title = "\nTodo CLI - Main Menu\n"

        menu = TerminalMenu(
            self.menu_items[menu_type],
            title=main_menu_title,
            menu_highlight_style=("fg_green",),
            cycle_cursor=True,
            clear_screen=True,
            skip_empty_entries=True,
            show_search_hint=False,
            status_bar=title,
            status_bar_style=("fg_yellow", "bold"),
        )
        return menu.show()

    def display_todo_selection_menu(
        self, todos: List[Todo], action: str
    ) -> Optional[Todo]:
        """
        Display a menu to select a todo and return the selected todo.

        Args:
            todos (List[Todo]): List of todos to choose from.
            action (str): The action being performed (e.g., "update", "complete").

        Returns:
            Optional[Todo]: The selected todo or None if no selection was made.
        """
        options = [f"[{todo.task_id}] {todo.task} ({todo.category})" for todo in todos]
        menu = TerminalMenu(
            options,
            title=f"\nSelect a todo to {action}",
            menu_highlight_style=("fg_green",),
            cycle_cursor=True,
            clear_screen=True,
        )
        index = menu.show()
        return todos[index] if index is not None else None

    def display_category_menu(self) -> Optional[str]:
        """
        Display a menu to select a category and return the selected category.

        Returns:
            Optional[str]: The selected category or None if no selection was made.
        """
        categories = self.gs.get_all_categories()
        options = [category["category_name"] for category in categories]
        menu = TerminalMenu(
            options,
            title="\nSelect a category",
            menu_highlight_style=("fg_green",),
            cycle_cursor=True,
            clear_screen=True,
        )
        index = menu.show()
        return options[index] if index is not None else None

    def add_todo(self):
        """Add a new todo item."""
        console.print(Panel.fit("\nAdd New Todo", style="bold green"))
        task = self.get_input("Enter the task", required=True)
        category = self.display_category_menu()
        if category is None:
            console.print("\n[bold yellow]Todo addition cancelled.[/bold yellow]")
            return
        due_date = self.get_due_date()
        todo = Todo(task=task, category=category, due_date=due_date)
        try:
            self.gs.insert_todo(todo)
            console.print("\n[bold green]Todo added successfully![/bold green]")
        except Exception as e:
            console.print(f"\n[bold red]Error adding todo: {str(e)}[/bold red]")

    def show_todos(self):
        """Display all todos in a table format."""
        try:
            tasks = self.gs.get_all_todos()
            if not tasks:
                console.print("\n[bold yellow]No To-Do's found.[/bold yellow]")
                return

            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("ID", style="dim", width=6, justify="center")
            table.add_column("Todo", min_width=20)
            table.add_column("Category", min_width=12, justify="center")
            table.add_column("Added", min_width=10, justify="center")
            table.add_column("Due Date", min_width=10, justify="center")
            table.add_column("Completed", min_width=10, justify="center")

            for task in tasks:
                c = self.get_category_color(task.category)
                due_date = (
                    datetime.fromisoformat(task.due_date).date()
                    if task.due_date
                    else None
                )
                due_date_str = due_date.isoformat() if due_date else "-"

                # Determine the status and color for the 'Completed' column
                if task.date_completed:
                    completion_date = datetime.fromisoformat(task.date_completed).date()
                    status = completion_date.isoformat()
                    if due_date and completion_date > due_date:
                        status_color = "red"  # Completed late
                    else:
                        status_color = "green"  # Completed on time or early
                elif due_date and due_date < datetime.now().date():
                    status = "OVERDUE"
                    status_color = "red"
                else:
                    status = "-"
                    status_color = "white"

                table.add_row(
                    str(task.task_id),
                    task.task,
                    f"[{c}]{task.category}[/{c}]",
                    task.date_added[:10],
                    due_date_str,
                    f"[{status_color}]{status}[/{status_color}]",
                )

            console.print(
                Panel(table, title="\n[bold]Your Todo List[/bold]", expand=False)
            )
        except Exception as e:
            console.print(f"\n[bold red]Error fetching todos: {str(e)}[/bold red]")

    def update_todo(self):
        """Update an existing todo item."""
        try:
            todos = self.gs.get_all_todos()
            if not todos:
                console.print("\n[bold yellow]No todos found.[/bold yellow]")
                return

            selected_todo = self.display_todo_selection_menu(todos, "update")
            if selected_todo is None:
                console.print("\n[bold yellow]Update cancelled.[/bold yellow]")
                return

            console.print(
                Panel.fit(f"Updating: {selected_todo.task}", style="bold yellow")
            )
            task = self.get_input(f"Enter the new task (current: {selected_todo.task})")
            category = self.display_category_menu()
            due_date = self.get_due_date(current=selected_todo.due_date)

            self.gs.update_todo(selected_todo.task_id, task, category, due_date)
            console.print("\n[bold green]Todo updated successfully![/bold green]")
        except Exception as e:
            console.print(f"\n[bold red]Error updating todo: {str(e)}[/bold red]")

    def complete_todo(self):
        """Mark a todo item as completed."""
        try:
            todos = [
                todo for todo in self.gs.get_all_todos() if not todo.date_completed
            ]
            if not todos:
                console.print("\n[bold yellow]No incomplete todos found.[/bold yellow]")
                return

            selected_todo = self.display_todo_selection_menu(todos, "complete")
            if selected_todo is None:
                console.print("\n[bold yellow]Completion cancelled.[/bold yellow]")
                return

            if self.confirm_action(
                f"\nAre you sure you want to mark '{selected_todo.task}' as complete?"
            ):
                self.gs.complete_todo(selected_todo.task_id)
                console.print("\n[bold green]Todo marked as complete![/bold green]")
            else:
                console.print("\n[bold yellow]Action cancelled.[/bold yellow]")
        except Exception as e:
            console.print(f"\n[bold red]Error completing todo: {str(e)}[/bold red]")

    def delete_todo(self):
        """Delete a todo item."""
        try:
            todos = self.gs.get_all_todos()
            if not todos:
                console.print("\n[bold yellow]No todos found.[/bold yellow]")
                return

            selected_todo = self.display_todo_selection_menu(todos, "delete")
            if selected_todo is None:
                console.print("\n[bold yellow]Deletion cancelled.[/bold yellow]")
                return

            if self.confirm_action(
                f"\nAre you sure you want to delete '{selected_todo.task}'?"
            ):
                self.gs.delete_todo(selected_todo.task_id)
                console.print("\n[bold green]Todo deleted successfully![/bold green]")
            else:
                console.print("\n[bold yellow]Deletion cancelled.[/bold yellow]")
        except Exception as e:
            console.print(f"\n[bold red]Error deleting todo: {str(e)}[/bold red]")

    def show_statistics(self):
        """Display statistics about the todos."""
        try:
            todos = self.gs.get_all_todos()
            total_todos = len(todos)
            completed_todos = sum(1 for todo in todos if todo.date_completed)
            overdue_todos = sum(
                1
                for todo in todos
                if not todo.date_completed
                and todo.due_date
                and datetime.fromisoformat(todo.due_date).date() < datetime.now().date()
            )

            categories = set(todo.category for todo in todos)
            category_stats = {
                category: sum(1 for todo in todos if todo.category == category)
                for category in categories
            }

            console.print(Panel.fit("\n[bold]Todo Statistics[/bold]", style="cyan"))
            console.print(f"Total Todos: {total_todos}")
            console.print(f"Completed Todos: {completed_todos}")
            console.print(f"Overdue Todos: {overdue_todos}")
            console.print("\nTodos by Category:")
            for category, count in category_stats.items():
                console.print(f"  {category}: {count}")

        except Exception as e:
            console.print(f"\n[bold red]Error fetching statistics: {str(e)}[/bold red]")

    def get_input(self, prompt: str, required: bool = False) -> Optional[str]:
        """Get user input with optional requirement."""
        while True:
            value = console.input(f"\n[bold cyan]{prompt}:[/bold cyan] ").strip()
            if value or not required:
                return value or None
            console.print(
                "\n[bold red]This field cannot be empty. Please try again.[/bold red]"
            )

    def get_due_date(self, current: Optional[str] = None) -> Optional[str]:
        """Get due date input from the user."""
        while True:
            date_str = self.get_input(
                f"Enter due date (YYYY-MM-DD) or press Enter to skip{' or keep current' if current else ''}"
            )
            if not date_str:
                return current
            try:
                due_date = datetime.strptime(date_str, "%Y-%m-%d").date()
                return due_date.isoformat()
            except ValueError:
                console.print(
                    "\n[bold red]Invalid date format. Please use YYYY-MM-DD.[/bold red]"
                )

    def confirm_action(self, message: str) -> bool:
        """Confirm an action with the user."""
        console.print(f"[bold yellow]{message}[/bold yellow]")
        choice = self.display_menu("confirm", "\nConfirm Action")
        return choice == 0  # "Yes" is the first option

    @staticmethod
    def get_category_color(category: str) -> str:
        """Get the color for a category."""
        colors = {
            "Coding": "bright_cyan",
            "CI-Stuff": "yellow",
            "Personal": "bright_blue",
            "Study": "bright_white",
            "Errands": "bright_black",
        }
        return colors.get(category, "white")

