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

