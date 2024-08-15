from mvp import TodoCLI
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box
import os

console = Console()

def clear_terminal():
    """
    Function to clear the terminal screen
    """
    os.system("cls" if os.name == "nt" else "clear")

def display_welcome_screen():
    """Display a welcome screen with app information and instructions."""
    title = Text("Welcome to Task Tracker CLI", style="bold cyan")
    subtitle = Text("Your Command-Line To-do Manager", style="italic magenta")

    info = Text.assemble(
        ("• Efficiently manage your tasks from the command line\n"),
        ("• Organize tasks by categories\n"),
        ("• Set due dates and track task completion\n"),
        ("• View task statistics and stay productive\n"),
        style="green",
    )

    instructions = Text("Press Enter to start, or 'q' to quit", style="yellow")

    welcome_panel = Panel(
        Text.assemble(
            title, "\n\n", subtitle, "\n\n", info, "\n", instructions
            ),
        box=box.ROUNDED,
        expand=False,
        border_style="bright_blue",
        padding=(1, 1),
    )

    console.print(welcome_panel)


def start_app():
    """Start the Todo CLI application."""
    while True:
        display_welcome_screen()
        user_input = console.input().strip().lower()
        clear_terminal()

        if user_input == "q":
            console.print(
                "[bold red]Exiting Task Tracker CLI. Goodbye![/bold red]\n"
                )
            break
        elif user_input == "":
            console.print(
                "[bold green]Starting Task Tracker CLI...[/bold green]\n"
                )
            TodoCLI().run()
            break
        else:
            console.print(
                "[bold red]Invalid input. Please try again.[/bold red]\n"
                )


if __name__ == "__main__":
    start_app()
