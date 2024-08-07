import sqlite3
from typing import List, Optional
import datetime
from model import Todo

DATABASE_NAME = "todos.db"


def get_db_connection():
    return sqlite3.connect(DATABASE_NAME)


def create_table():
    """Create the todos table if it doesn't exist."""
    pass


def insert_todo():
    """Insert a new todo into the database."""
    pass


def get_all_todos():
    """Retrieve all todos from the database."""
    pass


def update_todo():
    """Update a todo's task, category, and/or due date."""
    pass


def delete_todo():
    """Delete a todo and update positions of remaining todos."""
    pass


def complete_todo():
    """Mark a todo as completed."""
    pass


# Initialize the database
create_table()
