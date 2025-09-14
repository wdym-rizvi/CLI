from rich import print
from datetime import datetime

def run():
    print("[bold cyan]Fetching current time...[/bold cyan]")
    try:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[bold green]Current Time:[/bold green] {now}")
    except Exception as e:
        print(f"[bold red]Error fetching time:[/bold red] {e}")
