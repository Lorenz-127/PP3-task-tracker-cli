import gspread
from google.oauth2.service_account import Credentials
from typing import List, Dict, Any, Optional
from model import Todo
from datetime import datetime


class TodoGoogleSheets:
    """Class for managing Todo List operations with Google Sheets."""

    SCOPE = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive",
    ]

    def __init__(self, creds_file: str = "creds.json"):
        """
        Initialize the TodoGoogleSheets class.

        :param creds_file: Path to the credentials JSON file (default: "creds.json")
        """
        self.creds = Credentials.from_service_account_file(creds_file)
        self.scoped_creds = self.creds.with_scopes(self.SCOPE)
        self.client = gspread.authorize(self.scoped_creds)
        self.sheet = self.client.open("task_tracker")
        self.tasks_worksheet = self.sheet.worksheet("tasks")
        self.categories_worksheet = self.sheet.worksheet("categories")

