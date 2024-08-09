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

    def insert_todo(self, todo: Todo) -> None:
        """Insert a new todo into the Google Sheet."""
        task_id = self.get_next_task_id()
        category_id = self.get_category_id(todo.category)
        position = self.get_next_position()
        self.tasks_worksheet.append_row(
            [
                task_id,
                todo.task,
                category_id,
                todo.date_added or datetime.now().isoformat(),
                todo.due_date,
                todo.date_completed,
                position,
            ]
        )

    def update_todo(
        self,
        task_id: int,
        task: Optional[str] = None,
        category: Optional[str] = None,
        due_date: Optional[str] = None,
    ) -> None:
        """Update a todo's task, category, and/or due date."""
        row = self.find_row_by_task_id(task_id)
        updates = []
        if task is not None:
            updates.append({"range": f"B{row}", "values": [[task]]})
        if category is not None:
            category_id = self.get_category_id(category)
            updates.append({"range": f"C{row}", "values": [[category_id]]})
        if due_date is not None:
            updates.append({"range": f"E{row}", "values": [[due_date]]})

        if updates:
            self.tasks_worksheet.batch_update(updates)

