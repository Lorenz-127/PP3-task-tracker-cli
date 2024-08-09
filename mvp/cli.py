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

