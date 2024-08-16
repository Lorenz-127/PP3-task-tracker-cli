import pytest
from unittest.mock import patch, MagicMock
from mvp.cli import TodoCLI
from mvp.model import Todo


# Mock time.sleep for all tests
@pytest.fixture(autouse=True)
def no_sleep(monkeypatch):
    monkeypatch.setattr('time.sleep', lambda x: None)


@pytest.fixture
def todo_cli():
    """
    Fixture to create a TodoCLI instance with a mocked GoogleSheets backend.
    This allows for isolated testing of the CLI functionality.
    """
    with patch('mvp.cli.TodoGoogleSheets') as mock_gs:
        cli = TodoCLI()
        cli.gs = mock_gs
        yield cli


@pytest.fixture
def mock_todos():
    """
    Fixture to create a list of mock Todo objects.
    This provides consistent test data across multiple tests.
    """
    return [
        Todo(task_id=1, task="Task 1", category="Category 1"),
        Todo(task_id=2, task="Task 2", category="Category 2"),
    ]


@pytest.mark.usefixtures("todo_cli")
class TestTodoCLI:
    @classmethod
    def setup_class(cls):
        # Perform any one-time setup here
        pass

