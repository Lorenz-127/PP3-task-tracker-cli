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

    def delete_todo(self, task_id: int) -> None:
        """Delete a todo and update positions of remaining todos."""
        row = self.find_row_by_task_id(task_id)
        self.tasks_worksheet.delete_rows(row)
        self.update_positions()

    def complete_todo(self, task_id: int) -> None:
        """Mark a todo as completed."""
        row = self.find_row_by_task_id(task_id)
        self.tasks_worksheet.update_cell(row, 6, datetime.now().isoformat())

    def get_todos_by_category(self, category: str) -> List[Todo]:
        """Get all todos for a specific category."""
        all_todos = self.get_all_todos()
        return [todo for todo in all_todos if todo.category == category]

    def get_overdue_todos(self) -> List[Todo]:
        """Get all overdue todos."""
        all_todos = self.get_all_todos()
        today = datetime.now().date()
        return [
            todo
            for todo in all_todos
            if todo.due_date
            and datetime.fromisoformat(todo.due_date).date() < today
            and not todo.date_completed
        ]

    def get_next_task_id(self) -> int:
        """Get the next available task_id."""
        task_ids = self.tasks_worksheet.col_values(1)[1:]  # Exclude header
        return max(map(int, task_ids or [0])) + 1

    def get_next_position(self) -> int:
        """Get the next available position."""
        positions = self.tasks_worksheet.col_values(7)[1:]  # Exclude header
        return max(map(int, positions or [0])) + 1

    def find_row_by_task_id(self, task_id: int) -> int:
        """Find the row number for a given task_id."""
        cell = self.tasks_worksheet.find(str(task_id), in_column=1)
        if cell is None:
            raise ValueError(f"Task with id {task_id} not found")
        return cell.row

    def get_category_id(self, category_name: str) -> int:
        """Get the category_id for a given category name."""
        categories = self.categories_worksheet.get_all_records()
        for category in categories:
            if category["category_name"] == category_name:
                return category["category_id"]
        raise ValueError(f"Category '{category_name}' not found")

    def add_category(self, category_name: str) -> None:
        """Add a new category."""
        category_id = self.get_next_category_id()
        self.categories_worksheet.append_row([category_id, category_name])

    def get_next_category_id(self) -> int:
        """Get the next available category_id."""
        category_ids = self.categories_worksheet.col_values(1)[1:]  # Exclude header
        return max(map(int, category_ids or [0])) + 1

    def update_positions(self) -> None:
        """Update positions after a todo is deleted."""
        todos = self.get_all_todos()
        updates = [{"range": f"G{i+2}", "values": [[i + 1]]} for i in range(len(todos))]
        self.tasks_worksheet.batch_update(updates)

    def reorder_todo(self, task_id: int, new_position: int) -> None:
        """Change the position of a todo."""
        todos = self.get_all_todos()
        todos.sort(key=lambda x: x.position)

        todo_to_move = next(todo for todo in todos if todo.task_id == task_id)
        old_position = todo_to_move.position

        if old_position < new_position:
            for todo in todos:
                if old_position < todo.position <= new_position:
                    self.update_position(todo.task_id, todo.position - 1)
        else:
            for todo in todos:
                if new_position <= todo.position < old_position:
                    self.update_position(todo.task_id, todo.position + 1)

        self.update_position(task_id, new_position)

    def update_position(self, task_id: int, new_position: int) -> None:
        """Update the position of a specific todo."""
        row = self.find_row_by_task_id(task_id)
        self.tasks_worksheet.update_cell(row, 7, new_position)

