from dataclasses import dataclass, field
from datetime import datetime, date
from typing import Optional

@dataclass
class Todo:
    task: str
    category: str
    date_added: str = field(default_factory=lambda: datetime.now().isoformat())
    date_completed: Optional[str] = None
    due_date: Optional[str] = None
    status: int = 1  # 1 = open, 2 = completed
    position: Optional[int] = None

    def __post_init__(self):
        if self.status not in [1, 2]:
            raise ValueError("Status must be 1 (open) or 2 (completed)")
        if self.due_date and not isinstance(self.due_date, str):
            self.due_date = self.due_date.isoformat()

    def __str__(self) -> str:
        status = 'Completed' if self.status == 2 else 'Open'
        due = f", Due: {self.due_date}" if self.due_date else ""
        return f"Task: {self.task}, Category: {self.category}, Status: {status}{due}"