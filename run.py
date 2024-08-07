import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from simple_term_menu import TerminalMenu
from model import Todo
from database import get_all_todos, delete_todo, insert_todo, complete_todo, update_todo
from datetime import datetime, date


class TodoCLI:
    def __init__(self):
        """
        Initialize the TodoCLI with menu items.
        """

    def display_menu(self):
        """
        Display a menu of the specified type and return the selected option.

        Args:
            menu_type (str): The type of menu to display.
            title (str): The title of the menu.

        Returns:
            int: The index of the selected menu item.
        """

    def add_todo(self):
        """
        Prompt the user to update an existing todo task.
        """

    def show_todos(self):
        """
        Display all the todos in a table format.
        """

    def update_todo(self):
        """ Prompt the user to update a todo. """

    def get_due_date(self):
        """
        Prompt the user to enter a due date for a todo task.

        Args:
            current (str, optional): The current due date. Defaults to None.

        Returns:
            str: The entered due date.
        """

    def complete_todo(self):
        """
        Prompt the user to mark a todo task as complete.
        """

    def delete_todo(self):
        """
        Prompt the user to delete an existing todo task.
        """

    def confirm_action(self):
        """
        Prompt the user to confirm an action.

        Args:
            message (str): The confirmation message.

        Returns:
            bool: True if the user confirms, False otherwise.
        """

    @staticmethod
    def get_category_color(category):
        """
        Return the color associated with a category.

        Args:
            category (str): The category name.

        Returns:
            str: The color associated with the category.
        """

    def run(self):
        """
        Run the Todo CLI application with a menu-driven interface.
        """

@app.command()
def main():
    """
    Run the Todo CLI application.
    """
    TodoCLI().run()

if __name__ == "__main__":
    app()