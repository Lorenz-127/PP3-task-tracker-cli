from dataclasses import dataclass, asdict
from datetime import datetime, date
from typing import Optional, Dict, Any


@dataclass
class Todo:
    """
    Represents a Todo item in the task management system.

    Attributes:
        task (str):
        The description of the todo task.
        category (str):
        The category to which the task belongs.
        task_id (Optional[int]):
        Unique identifier for the task. Defaults to None.
        date_added (Optional[str]):
        The date when the task was added. Defaults to None.
        due_date (Optional[str]):
        The due date for the task. Defaults to None.
        date_completed (Optional[str]):
        The date when the task was completed. Defaults to None.
        position (Optional[int]):
        The position of the task in the list. Defaults to None.
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
        Post-initialization method to validate and convert date fields.
        """
        self._validate_dates()
        self._convert_dates_to_iso()

    def _validate_dates(self):
        """
        Basic validation for date fields.

        Raises:
            ValueError:
            If a date field is neither a string nor a date/datetime object.
        """
        for field in ["date_added", "due_date", "date_completed"]:
            value = getattr(self, field)
            if value and not isinstance(value, (str, date, datetime)):
                raise ValueError(
                    f"{field} must be a string, date, or datetime object"
                )

    def _convert_dates_to_iso(self):
        """
        Convert date fields to ISO format strings.
        """
        for field in ["date_added", "due_date", "date_completed"]:
            value = getattr(self, field)
            if isinstance(value, (date, datetime)):
                setattr(self, field, value.isoformat())

    @property
    def status(self) -> str:
        """
        Returns the status of the todo item.

        Returns:
            str:
            'Completed' if the task has a completion date, otherwise 'Open'.
        """
        return "Completed" if self.date_completed else "Open"

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the Todo object to a dictionary.

        Returns:
            Dict[str, Any]: A dictionary representation of the Todo object.
        """
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Todo":
        """
        Create a Todo instance from a dictionary.

        Args:
            data (Dict[str, Any]): A dictionary containing Todo data.

        Returns:
            Todo: A new Todo instance created from the provided dictionary.
        """
        return cls(**data)

    def __str__(self) -> str:
        """
        Returns a string representation of the Todo item.

        Returns:
            str: A formatted string containing task details.
        """
        due = f", Due: {self.due_date}" if self.due_date else ""
        return (
            f"Task: {self.task}, Category: {self.category}, "
            f"Status: {self.status}{due}"
        )
