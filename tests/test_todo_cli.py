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

    def test_add_todo(self, todo_cli):
        """
        Test the add_todo method of TodoCLI.
        This test ensures that a new todo can be added correctly,
        with the right task, category, and due date.
        """
        with patch('mvp.cli.console.input', return_value="Test task"), \
             patch(
                 'mvp.cli.TodoCLI.display_category_menu',
                 return_value="Test category"), \
             patch('mvp.cli.TodoCLI.get_due_date', return_value="2023-12-31"):
            todo_cli.add_todo()

        todo_cli.gs.insert_todo.assert_called_once()
        inserted_todo = todo_cli.gs.insert_todo.call_args[0][0]

        assert isinstance(inserted_todo, Todo)
        assert inserted_todo.task == "Test task"
        assert inserted_todo.category == "Test category"
        assert inserted_todo.due_date == "2023-12-31"

    def test_show_todos(self, todo_cli, mock_todos):
        """
        Test the show_todos method of TodoCLI.
        This test verifies that the method correctly retrieves and displays
        all todos from the Google Sheets backend.
        """
        todo_cli.gs.get_all_todos.return_value = mock_todos
        with patch('mvp.cli.console.print') as mock_print:
            todo_cli.show_todos()
            mock_print.assert_called()

    def test_complete_todo(self, todo_cli, mock_todos):
        """
        Test the complete_todo method of TodoCLI.
        This test ensures that a selected todo can be marked as complete,
        and that the appropriate method is called on the backend.
        """
        todo_cli.gs.get_all_todos.return_value = mock_todos
        with patch.multiple(
            'mvp.cli.TodoCLI',
            display_todo_selection_menu=MagicMock(return_value=mock_todos[0]),
            confirm_action=MagicMock(return_value=True)
        ):
            todo_cli.complete_todo()
            todo_cli.gs.complete_todo.assert_called_once_with(1)

    @pytest.mark.parametrize("input_value, required, expected", [
        ("Test input", False, "Test input"),
        ("Valid input", True, "Valid input"),
        ("", False, None),  # Changed from "" to None
    ])
    def test_get_input(self, todo_cli, input_value, required, expected):
        """
        Test the get_input method of TodoCLI with various input scenarios.

        This test function verifies the behavior of the get_input method
        under different conditions, including optional and required inputs,
        as well as empty input handling.

        Args:
            todo_cli (TodoCLI): The TodoCLI instance being tested.
            input_value (str): The simulated user input value.
            required (bool): Whether the input is required or optional.
            expected (str or None): The expected return value from get_input.

        Scenarios tested:
        1. Optional input with a non-empty value
        2. Required input with a valid value
        3. Optional input with an empty value (should return None)

        The test uses pytest's parametrize decorator to run multiple test cases
        with different inputs and expected outputs.

        Raises:
            AssertionError: If the result of get_input does not match the expected value.
        """
        with patch('mvp.cli.console.input', return_value=input_value):
            result = todo_cli.get_input("Enter input: ", required=required)
            assert result == expected

    def test_get_input_required_empty_then_valid(self, todo_cli):
        """
        Test the get_input method when a required field is initially empty.
        This test ensures that the method prompts for input again
        when a required field is left empty,
        and accepts valid input afterwards. 
        """
        with patch('mvp.cli.console.input') as mock_input:
            mock_input.side_effect = ["", "Valid input"]
            result = todo_cli.get_input("Enter input: ", required=True)
            assert result == "Valid input"
            assert mock_input.call_count == 2

    @pytest.mark.timeout(10)
    def test_add_todo_with_invalid_input(self, todo_cli):
        """
        Test adding a todo with invalid (empty) input.
        This test verifies that the add_todo method
        handles empty input correctly,
        ensuring that no todo is added to the backend in this case.
        """
        print("Starting test_add_todo_with_invalid_input")
        with patch('mvp.cli.console.input', return_value=""):
            print("Calling todo_cli.add_todo()")
            todo_cli.add_todo()
            print("Finished calling todo_cli.add_todo()")
        print("Asserting insert_todo was not called")
        todo_cli.gs.insert_todo.assert_not_called()
        print("Test completed")

