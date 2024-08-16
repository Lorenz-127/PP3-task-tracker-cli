from typing import List, Optional
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from simple_term_menu import TerminalMenu
from .model import Todo
from .google_sheets_db import TodoGoogleSheets
from datetime import datetime, date
import sys
import time
from gspread.exceptions import SpreadsheetNotFound

console = Console()

MAX_INPUT_LENGTH = 50


class TodoCLI:
    """
    A command-line interface for managing todos
    using Google Sheets as a backend.

    This class provides methods for adding, viewing, updating, completing,
    and deleting todos, as well as displaying statistics. It uses Rich for
    enhanced console output and simple-term-menu for interactive menus.

    Attributes:
        menu_items (dict):
        A dictionary containing menu options for different actions.

        gs (TodoGoogleSheets):
        An instance of TodoGoogleSheets for database operations.

    Raises:
        SpreadsheetNotFound:
        If the required Google Sheets spreadsheet is not accessible.

        Exception: For other unexpected errors during initialization.
    """
    def __init__(self):
        """
        Initialize the TodoCLI with menu items and Google Sheets integration.

        This method sets up the menu structure and establishes a connection
        to Google Sheets. It handles potential errors during initialization
        and provides appropriate feedback to the user.

        Raises:
            SpreadsheetNotFound:
            If the Google Sheets spreadsheet is not found or accessible.

            Exception: For any other unexpected errors during initialization.
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
        try:
            self.gs = TodoGoogleSheets()
        except SpreadsheetNotFound as e:
            console.print(
                Panel.fit(
                    f"[bold red]Error:[/bold red] {str(e)}\n\n"
                    "The required Google Sheets spreadsheet"
                    "could not be found or accessed.\n"
                    "Please check the following:\n"
                    "1. The spreadsheet 'task_tracker'"
                    "exists in your Google Drive\n"
                    "2. You have the correct permissions to access it\n"
                    "3. Your Google API credentials"
                    "are correct and up to date\n\n"
                    "If the problem persists, please contact"
                    "the system administrator.",
                    title="Google Sheets Connection Error",
                    border_style="red",
                )
            )
            sys.exit(1)
        except Exception as e:
            console.print(
                Panel.fit(
                    f"[bold red]An unexpected error"
                    f"occurred:[/bold red]\n{str(e)}\n\n"
                    "This could be due to:\n"
                    "1. Network connectivity issues\n"
                    "2. Invalid or expired Google API credentials\n"
                    "3. Insufficient permissions\n\n"
                    "Please check your internet connection"
                    "and configuration.\n"
                    "If the problem persists, please contact"
                    "the system administrator.",
                    title="Initialization Error",
                    border_style="red",
                )
            )
            sys.exit(1)

        console.print(
            Panel.fit(
                "[green]Successfully connected to Google Sheets![/green]\n"
                "You can now start managing your tasks.",
                title="Initialization Complete",
                border_style="green",
            )
        )
        time.sleep(3)

    def display_menu(self, menu_type: str, title: str) -> int:
        """
        Display a menu of the specified type and return the selected option.

        This method uses simple-term-menu to create an interactive CLI menu.

        Args:
            menu_type (str): The type of menu to display ('main' or 'confirm').
            title (str): The title to display above the menu.

        Returns:
            int: The index of the selected menu item.

        Note:
            Returns None if the user cancels the selection.
        """""
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
        Display a menu to select a single todo and return the selected todo.

        This method creates an interactive menu for the user to choose a todo
        from a list of todos for a specific action (e.g., update, complete).

        Args:
            todos (List[Todo]):
            List of todos to choose from.

            action (str):
            The action being performed (e.g., "update", "complete").

        Returns:
            Optional[Todo]: The selected todo or None if no selection was made
                            or user chose to return to main menu.
        """
        if not todos:
            console.print(Panel.fit(
                "\n[bold yellow]No todos available.[/bold yellow]")
            )
            return None

        options = [
            f"{i+1:2d}. {todo.task[:40]:40} ({todo.category})"
            for i, todo in enumerate(todos)
        ]
        options.append("[Return to Main Menu]")

        menu = TerminalMenu(
            options,
            title=f"\nSelect a todo to {action}",
            menu_highlight_style=("fg_green",),
            cycle_cursor=True,
            clear_screen=True,
            show_search_hint=True,
        )

        index = menu.show()
        if index is None or index == len(todos):
            return None
        return todos[index]

    def display_category_menu(self) -> Optional[str]:
        """
        Display a menu to select a category and return the selected category.

        This method retrieves all categories from the database and presents
        them in an interactive menu for the user to choose from.

        Returns:
            Optional[str]:
            The selected category name or None if no selection was made.
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
        """
        Add a new todo item to the task list.

        This method prompts the user for task details,
        including the task description, category, and due date.
        It then creates a new Todo object and inserts it into
        the Google Sheets database.

        The method handles potential errors and
        provides feedback to the user on the
        success or failure of the operation.

        Raises:
            ValueError:
            If there's an issue with the input data.

            Exception:
            For any unexpected errors during the todo addition process.
        """
        console.print(Panel.fit("\nAdd New Todo", style="bold green"))
        task = self.get_input("Enter the task", required=True, max_length=50)
        if task is None:
            console.print(
                "\n[bold yellow]Todo addition cancelled.[/bold yellow]"
            )
            return
        category = self.display_category_menu()
        if category is None:
            console.print(
                "\n[bold yellow]Todo addition cancelled.[/bold yellow]"
            )
            return
        try:
            due_date = self.get_due_date()
            todo = Todo(task=task, category=category, due_date=due_date)
            self.gs.insert_todo(todo)
            console.print(
                "\n[bold green]Todo added successfully![/bold green]"
            )
        except ValueError as e:
            console.print(
                f"\n[bold red]Error adding todo: {str(e)}[/bold red]"
            )
        except Exception as e:
            console.print(
                f"\n[bold red]An unexpected error "
                f"occurred: {str(e)}[/bold red]"
            )
            console.print(
                "Please try again or contact support if the problem persists."
            )

    def show_todos(self):
        """
        Display all todos in a formatted table.

        This method retrieves all todos from
        the database and presents them in a Rich table format.
        It includes task details, categories (color-coded),
        due dates, and completion status.

        The method handles potential errors
        in fetching or displaying the todos.

        Raises:
            Exception:
            For any unexpected errors during the retrieval or display process.
        """
        try:
            tasks = self.gs.get_all_todos()
            if not tasks:
                console.print("\n[bold yellow]No To-Do's found.[/bold yellow]")
                return

            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("ID", style="dim", width=4, justify="right")
            table.add_column("Todo", min_width=22)
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
                    completion_date = (
                        datetime.fromisoformat(task.date_completed).date()
                    )
                    status = completion_date.isoformat()
                    if due_date and completion_date > due_date:
                        status_color = "red"  # Completed late
                    else:
                        status_color = "green"  # Completed on time or early
                elif due_date and due_date < datetime.now().date():
                    status = "OVERDUE"
                    status_color = "red"
                else:
                    status = "PENDING"
                    status_color = "green"

                table.add_row(
                    str(task.task_id),
                    task.task,
                    f"[{c}]{task.category}[/{c}]",
                    task.date_added[:10],
                    due_date_str,
                    f"[{status_color}]{status}[/{status_color}]",
                )

            console.print(
                Panel(
                    table,
                    title="\n[bold]Your Todo List[/bold]",
                    expand=False
                )
            )
        except Exception as e:
            console.print(
                f"\n[bold red]Error fetching todos: {str(e)}[/bold red]"
            )

    def update_todo(self):
        """
        Update an existing todo item.

        This method allows the user to select
        a todo from a list and update its
        details, including the task description,
        category, and due date.
        It then updates the todo in the Google Sheets database.

        The method handles potential errors and
        provides feedback to the user on the
        success or failure of the update operation.

        Raises:
            Exception: For any unexpected errors during the update process.
        """
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
                Panel.fit(
                    f"Updating: {selected_todo.task}", style="bold yellow"
                )
            )
            task = self.get_input(
                f"Enter the new task (current: {selected_todo.task})",
                max_length=50
            )
            category = self.display_category_menu()
            due_date = self.get_due_date(current=selected_todo.due_date)

            self.gs.update_todo(
                selected_todo.task_id, task, category, due_date
            )
            console.print(
                "\n[bold green]Todo updated successfully![/bold green]"
            )
        except Exception as e:
            console.print(
                f"\n[bold red]Error updating todo: {str(e)}[/bold red]"
            )

    def complete_todo(self):
        """
        Mark a todo item as completed.

        This method displays a list of incomplete todos
        for the user to select from.
        The selected todo is then marked as completed in the database.

        The method handles potential errors and
        provides feedback to the user on the
        success or failure of the completion operation.

        Raises:
            Exception:
            For any unexpected errors during the completion process.
        """
        try:
            todos = [
                todo for todo in self.gs.get_all_todos()
                if not todo.date_completed
            ]
            if not todos:
                console.print(
                    "\n[bold yellow]No incomplete todos found.[/bold yellow]"
                )
                return

            selected_todo = self.display_todo_selection_menu(todos, "complete")
            if selected_todo is None:
                console.print(
                    "\n[bold yellow]Completion cancelled.[/bold yellow]"
                )
                return

            if self.confirm_action(
                f"\nAre you sure you want to mark '{selected_todo.task}'"
                f"as complete?"
            ):
                self.gs.complete_todo(selected_todo.task_id)
                console.print(
                    "\n[bold green]Todo marked as complete![/bold green]"
                )
            else:
                console.print("\n[bold yellow]Action cancelled.[/bold yellow]")
        except Exception as e:
            console.print(
                f"\n[bold red]Error completing todo: {str(e)}[/bold red]"
            )

    def delete_todo(self):
        """
        Delete a todo item from the task list.

        This method allows the user to select a todo
        for deletion. It confirms the action with the user
        before permanently removing the todo from the database.

        The method handles potential errors and
        provides feedback to the user on the
        success or failure of the deletion operation.

        Raises:
            Exception:
            For any unexpected errors during the deletion process.
        """
        try:
            todos = self.gs.get_all_todos()
            if not todos:
                console.print("\n[bold yellow]No todos found.[/bold yellow]")
                return

            selected_todo = self.display_todo_selection_menu(todos, "delete")
            if selected_todo is None:
                console.print(
                    "\n[bold yellow]Deletion cancelled.[/bold yellow]"
                )
                return

            if self.confirm_action(
                f"\nAre you sure you want to delete '{selected_todo.task}'?"
            ):
                self.gs.delete_todo(selected_todo.task_id)
                console.print(
                    "\n[bold green]Todo deleted successfully![/bold green]"
                )
            else:
                console.print(
                    "\n[bold yellow]Deletion cancelled.[/bold yellow]"
                )
        except Exception as e:
            console.print(
                f"\n[bold red]Error deleting todo: {str(e)}[/bold red]"
            )

    def show_statistics(self):
        """
        Display statistics about the todos.

        This method calculates and presents various statistics about the todos,
        including total count, completed count, overdue count, and a breakdown
        by category.

        The method handles potential errors in
        fetching or calculating statistics.

        Raises:
            Exception:
            For any unexpected errors during the
            statistics calculation or display process.
        """
        try:
            todos = self.gs.get_all_todos()
            total_todos = len(todos)
            completed_todos = sum(1 for todo in todos if todo.date_completed)
            overdue_todos = sum(
                1 for todo in todos
                if not todo.date_completed
                and todo.due_date
                and datetime.fromisoformat(todo.due_date).date()
                < datetime.now().date()
            )

            categories = set(todo.category for todo in todos)
            category_stats = {
                category: sum(1 for todo in todos if todo.category == category)
                for category in categories
            }

            console.print(Panel.fit(
                "\n[bold]Todo Statistics[/bold]", style="cyan")
            )
            console.print(f"Total Todos: {total_todos}")
            console.print(f"Completed Todos: {completed_todos}")
            console.print(f"Overdue Todos: {overdue_todos}")
            console.print("\nTodos by Category:")
            for category, count in category_stats.items():
                console.print(f"  {category}: {count}")

        except Exception as e:
            console.print(
                f"\n[bold red]Error fetching statistics: {str(e)}[/bold red]"
            )

    def get_input(
        self,
        prompt: str,
        required: bool = False,
        max_length: int = MAX_INPUT_LENGTH,
        max_attempts: int = 3
    ) -> Optional[str]:
        """
        Get user input with optional requirement,
        maximum length constraint, and maximum attempts.

        Args:
            prompt (str):
                The prompt to display to the user.
            required (bool, optional):
                Whether the input is required. Defaults to False.
            max_length (int, optional):
                Maximum allowed length of the input.
                Defaults to MAX_INPUT_LENGTH.
            max_attempts (int, optional):
                Maximum number of attempts for input.
                Defaults to 3.

        Returns:
            Optional[str]:
                The user's input, or None if the input was
                invalid after max attempts.

        Note:
            Prompts the user up to max_attempts times for valid input.
        """
        for attempt in range(max_attempts):
            value = console.input(
                f"\n[bold cyan]{prompt}:[/bold cyan] "
            ).strip()

            if not value:
                if not required:
                    return None
                console.print(
                    "\n[bold red]This field cannot be empty. "
                    f"Attempts left: {max_attempts - attempt - 1}[/bold red]"
                )
                continue

            if len(value) > max_length:
                console.print(
                    f"\n[bold red]Input exceeds maximum length"
                    f"of {max_length} characters. "
                    f"Attempts left: {max_attempts - attempt - 1}[/bold red]"
                )
                continue

            return value

        console.print(
            "\n[bold yellow]Maximum attempts reached."
            "Input cancelled.[/bold yellow]"
        )
        return None

    def get_due_date(self, current: Optional[str] = None) -> Optional[str]:
        """
        Get due date input from the user.

        This method prompts the user to enter a
        due date for a todo item.
        It validates the input format and returns
        the date as an ISO formatted string.

        Args:
            current (Optional[str], optional):
            The current due date, if updating. Defaults to None.

        Returns:
            Optional[str]:
            The due date in ISO format (YYYY-MM-DD),
            or None if no date was entered.

        Raises:
            ValueError:
            If the entered date is in an invalid format.
        """
        while True:
            date_str = self.get_input(
                "Enter due date (YYYY-MM-DD) or press Enter to skip"
                f"{' or keep current' if current else ''}"
            )
            if not date_str:
                return current
            try:
                due_date = datetime.strptime(date_str, "%Y-%m-%d")
                return due_date.date().isoformat()
            except ValueError:
                console.print(
                    "\n[bold red]Invalid date format. "
                    "Please use YYYY-MM-DD.[/bold red]"
                )

    def confirm_action(self, message: str) -> bool:
        """
        Confirm an action with the user.

        This method displays a confirmation message to
        the user and prompts for a Yes/No response.

        Args:
            message (str): The confirmation message to display.

        Returns:
            bool: True if the user confirms the action, False otherwise.
        """
        console.print(f"[bold yellow]{message}[/bold yellow]")
        choice = self.display_menu("confirm", "\nConfirm Action")
        return choice == 0  # "Yes" is the first option

    @staticmethod
    def get_category_color(category: str) -> str:
        """
        Get the display color for a given category.

        Args:
            category (str): The name of the category.

        Returns:
            str: The color name to use for the given category.

        Note:
            Returns 'white' for any category
            not explicitly defined in the color mapping.
        """
        colors = {
            "Coding": "bright_cyan",
            "CI-Stuff": "yellow",
            "Personal": "bright_blue",
            "Study": "bright_white",
            "Errands": "bright_black",
        }
        return colors.get(category, "white")

    def run(self):
        """
        Run the main CLI loop.

        This method implements the main program loop, displaying the main menu
        and handling user choices. It continues running until the user chooses
        to exit the application.

        The method manages the flow between different operations like adding,
        showing, updating, completing,
        and deleting todos, as well as showing statistics.
        """
        while True:
            choice = self.display_menu(
                "main", "\nUse arrow keys to navigate, Enter to select"
            )
            if choice == 0:
                self.add_todo()
            elif choice == 1:
                self.show_todos()
            elif choice == 2:
                self.update_todo()
            elif choice == 3:
                self.complete_todo()
            elif choice == 4:
                self.delete_todo()
            elif choice == 5:
                self.show_statistics()
            elif choice == 7 or choice is None:
                if self.confirm_action("\nAre you sure you want to exit?"):
                    console.print(
                        "\n[bold green]Thank you for using Task Tracker CLI. "
                        "Goodbye![/bold green]"
                    )
                    break

            console.input("\nPress Enter to continue...")
