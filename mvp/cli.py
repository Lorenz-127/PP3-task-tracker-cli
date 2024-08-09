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

