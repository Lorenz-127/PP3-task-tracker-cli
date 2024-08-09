from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Todo:
    """
    Represents a Todo item with various attributes.

    Attributes:
        task (str): The description of the todo task.
        category (str): The category of the todo task.
        date_added (str): The date and time when the task was added (default: current time in ISO format).
        date_completed (Optional[str]): The date and time when the task was completed (default: None).
        due_date (Optional[str]): The due date for the task (default: None).
        status (int): The status of the task (1 = open, 2 = completed, default: 1).
        position (Optional[int]): The position of the task in a list (default: None).
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
        Performs post-initialization checks and conversions.

        Raises:
            ValueError: If the status is not 1 or 2.
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
