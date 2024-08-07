from dataclasses import dataclass, field
from datetime import datetime, date
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
    date_added: str = field(default_factory=lambda: datetime.now().isoformat())
    date_completed: Optional[str] = None
    due_date: Optional[str] = None
    status: int = 1
    position: Optional[int] = None

    def __post_init__(self):
        """
        Performs post-initialization checks and conversions.

        Raises:
            ValueError: If the status is not 1 or 2.
        """
        if self.status not in [1, 2]:
            raise ValueError("Status must be 1 (open) or 2 (completed)")
        if self.due_date and not isinstance(self.due_date, str):
            self.due_date = self.due_date.isoformat()

    def __str__(self) -> str:
        """
        Returns a string representation of the Todo item.

        Returns:
            str: A formatted string containing task details.
        """
        status = 'Completed' if self.status == 2 else 'Open'
        due = f", Due: {self.due_date}" if self.due_date else ""
        return f"Task: {self.task}, Category: {self.category}, Status: {status}{due}"