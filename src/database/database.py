import sqlite3
from typing import List, Optional
import datetime
from model import Todo


# Constants
DATABASE_NAME = "todos.db"


def get_db_connection():
    """
    Establish and return a connection to the SQLite database.

    Returns:
        sqlite3.Connection: A connection object to the SQLite database.
    """
    return sqlite3.connect(DATABASE_NAME)


def create_table():
    """
    Create the todos table if it doesn't exist.
    """
    pass


def insert_todo():
    """
    Insert a new todo into the database.
    """
    pass


def get_all_todos():
    """
    Retrieve all todos from the database.
    """
    pass


def update_todo():
    """
    Update a todo's task, category, and/or due date.

    Args:
        position (int): The position of the todo to update.
        task (Optional[str]): The new task description, if provided.
        category (Optional[str]): The new category, if provided.
        due_date (Optional[str]): The new due date, if provided.
    """
    pass


def delete_todo():
    """
    Delete a todo and update positions of remaining todos.

    Args:
        position (int): The position of the todo to delete.
    """
    pass


def complete_todo():
    """
    Mark a todo as completed.

    Args:
        position (int): The position of the todo to mark as completed.
    """
    pass


# Initialize the database
create_table()
