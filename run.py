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


    def display_menu(self):


    def add_todo(self):


    def show_todos(self):


    def update_todo(self):


    def get_due_date(self):


    def complete_todo(self):


    def delete_todo(self):


    def confirm_action(self):

    @staticmethod
    def get_category_color(category):


    def run(self):


@app.command()
def main():
    """
    Run the Todo CLI application.
    """


if __name__ == "__main__":
