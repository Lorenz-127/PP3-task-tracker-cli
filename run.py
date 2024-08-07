import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from simple_term_menu import TerminalMenu
from model import Todo
from database import get_all_todos, delete_todo, insert_todo, complete_todo, update_todo
from datetime import datetime, date


class TodoCLI:
    def __init__(self):
        """
        Initialize the TodoCLI with menu items.
        """
        self.menu_items = {
            "main": [
                "[1] Add Todo",
                "[2] Show Todo's",
                "[3] Update Todo",
                "[4] Complete Todo",
                "[5] Delete Todo",
                "",
                "[q] Exit",
            ],
            "confirm": ["Yes", "No"],
        }

    def display_menu(self, menu_type: str, title: str) -> int:
        """
        Display a menu of the specified type and return the selected option.

        Args:
            menu_type (str): The type of menu to display.
            title (str): The title of the menu.

        Returns:
            int: The index of the selected menu item.
        """
        # Main menu title
        main_menu_title = "\nTodo CLI - Main Menu\n"

        menu = TerminalMenu(
            self.menu_items[menu_type],
            title=main_menu_title,
            menu_highlight_style=("fg_green",),
            cycle_cursor=True,
            clear_screen=True,
            skip_empty_entries=True,  # Skip empty strings in the menu
            show_search_hint=False,  # Disable search hint
            status_bar=title,  # Use the title as a status bar instead
            status_bar_style=("fg_yellow", "bold"),
        )
        return menu.show()

        # Display the styled instruction text after the menu
        if menu_type == "main":
            console.print(Panel(title, style="yellow italic", expand=False))

        return result

    def add_todo(self):
        """
        Prompt the user to add a new todo task.

        This method guides the user through entering a task description,
        category, and due date for a new todo item. It performs input
        validation and inserts the new todo into the database.
        """
        console.print(Panel.fit("\nAdd New Todo", style="bold green"))
        while True:
            task = console.input("\n[bold cyan]Enter the task:[/bold cyan] ").strip()
            if task:
                break
            console.print(
                "\n[bold red]Task cannot be empty. Please try again.[/bold red]"
            )

        while True:
            category = console.input(
                "\n[bold cyan]Enter the category:[/bold cyan] "
            ).strip()
            if category:
                break
            console.print(
                "\n[bold red]Category cannot be empty. Please try again.[/bold red]"
            )

        due_date = self.get_due_date()
        todo = Todo(task, category, due_date=due_date)
        try:
            insert_todo(todo)
            console.print("\n[bold green]Todo added successfully![/bold green]\n")
        except Exception as e:
            console.print(f"\n[bold red]Error adding todo: {str(e)}[/bold red]\n")

    def show_todos(self):
        """
        Display all the todos in a table format.
        """
        tasks = get_all_todos()
        if not tasks:
            console.print("\n[bold yellow]No To-Do's found.[/bold yellow]\n")
            return

        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("#", style="dim", width=6, justify="center")
        table.add_column("Todo", min_width=20)
        table.add_column("Category", min_width=12, justify="center")
        table.add_column("Due Date", min_width=10)
        table.add_column("Added", min_width=10)
        table.add_column("Completed", min_width=10)
        table.add_column("Status", min_width=8, justify="center")

        for idx, task in enumerate(tasks, start=1):
            c = self.get_category_color(task.category)
            status = "✅" if task.status == 2 else "❌"
            date_completed = task.date_completed[:10] if task.date_completed else "-"
            due_date = task.due_date[:10] if task.due_date else "-"
            table.add_row(
                str(idx),
                task.task,
                f"[{c}]{task.category}[/{c}]",
                due_date,
                task.date_added[:10],
                date_completed,
                status,
            )

        console.print(
            Panel(table, title="\n[bold]Your Todo List[/bold]\n", expand=False)
        )

    def update_todo(self):
        """ Prompt the user to update a todo. """

    def get_due_date(self):
        """
        Prompt the user to enter a due date for a todo task.

        Args:
            current (str, optional): The current due date. Defaults to None.

        Returns:
            str: The entered due date.
        """

    def complete_todo(self):
        """
        Prompt the user to mark a todo task as complete.
        """

    def delete_todo(self):
        """
        Prompt the user to delete an existing todo task.
        """

    def confirm_action(self):
        """
        Prompt the user to confirm an action.

        Args:
            message (str): The confirmation message.

        Returns:
            bool: True if the user confirms, False otherwise.
        """

    @staticmethod
    def get_category_color(category):
        """
        Return the color associated with a category.

        Args:
            category (str): The category name.

        Returns:
            str: The color associated with the category.
        """

    def run(self):
        """
        Run the Todo CLI application with a menu-driven interface.
        """

@app.command()
def main():
    """
    Run the Todo CLI application.
    """
    TodoCLI().run()

if __name__ == "__main__":
    app()