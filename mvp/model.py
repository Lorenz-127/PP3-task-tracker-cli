from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Todo:
    """
    Represents a Todo item in the task management system.

    Attributes:
        task (str): The description of the todo task.
        category (str): The category to which the task belongs.
        task_id (Optional[int]): Unique identifier for the task. Defaults to None.
        date_added (Optional[str]): The date when the task was added. Defaults to None.
        due_date (Optional[str]): The due date for the task. Defaults to None.
        date_completed (Optional[str]): The date when the task was completed. Defaults to None.
        position (Optional[int]): The position of the task in the list. Defaults to None.
    """

    task: str
    category: str
    task_id: Optional[int] = None
    date_added: Optional[str] = None
    due_date: Optional[str] = None
    date_completed: Optional[str] = None
    position: Optional[int] = None

    def __post_init__(self):
        """
        Post-initialization method to ensure date fields are in ISO format strings.
        """
        # Convert due_date to ISO format string if it's not already a string
        if self.due_date and not isinstance(self.due_date, str):
            self.due_date = self.due_date.isoformat()

        # Convert date_completed to ISO format string if it's not already a string
        if self.date_completed and not isinstance(self.date_completed, str):
            self.date_completed = self.date_completed.isoformat()

    @property
    def status(self) -> str:
        """
        Returns the status of the todo item.

        Returns:
            str: 'Completed' if the task has a completion date, otherwise 'Open'.
        """
        return "Completed" if self.date_completed else "Open"

    def __str__(self) -> str:
        """
        Returns a string representation of the Todo item.

        Returns:
            str: A formatted string containing task details.
        """
        due = f", Due: {self.due_date}" if self.due_date else ""
        return (
            f"Task: {self.task}, Category: {self.category}, Status: {self.status}{due}"
        )
