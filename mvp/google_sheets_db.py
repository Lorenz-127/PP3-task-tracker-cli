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

    def get_all_todos(self) -> List[Todo]:
        """Retrieve all todos from the Google Sheet."""
        data = self.tasks_worksheet.get_all_records()
        categories = {
            row["category_id"]: row["category_name"]
            for row in self.categories_worksheet.get_all_records()
        }
        return [
            Todo(
                task_id=item["task_id"],
                task=item["task"],
                category=categories[item["category_id"]],
                date_added=item["date_added"],
                due_date=item["due_date"],
                date_completed=item["date_completed"],
                position=item["position"],
            )
            for item in data
        ]

