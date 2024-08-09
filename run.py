from mvp import TodoCLI
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box

console = Console()

def display_welcome_screen():
    """Display a welcome screen with app information and instructions."""
    title = Text("Welcome to Task Tracker CLI", style="bold cyan")
    subtitle = Text("Your Command-Line To-do Manager", style="italic magenta")
    
    info = Text.assemble(
        ("• Efficiently manage your tasks from the command line\n"),
        ("• Organize tasks by categories\n"),
        ("• Set due dates and track task completion\n"),
        ("• View task statistics and stay productive\n"),
        style="green"
    )
    
    instructions = Text("Press Enter to start, or 'q' to quit", style="yellow")
    
    welcome_panel = Panel(
        Text.assemble(title, "\n\n", subtitle, "\n\n", info, "\n", instructions),
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
        
        if user_input == 'q':
            console.print("[bold red]Exiting Todo CLI. Goodbye![/bold red]")
            break
        elif user_input == '':
            console.print("[bold green]Starting Todo CLI...[/bold green]")
            TodoCLI().run()
            break
        else:
            console.print("[bold red]Invalid input. Please try again.[/bold red]")

if __name__ == "__main__":
    start_app()