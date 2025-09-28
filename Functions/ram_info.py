from rich import print
import psutil

def run():
    print("[bold cyan]Fetching RAM usage...[/bold cyan]")
    try:
        mem = psutil.virtual_memory()
        print(f"[green]Total RAM:[/green] {mem.total / (1024**3):.2f} GB")
        print(f"[green]Available RAM:[/green] {mem.available / (1024**3):.2f} GB")
        print(f"[green]Used RAM:[/green] {mem.used / (1024**3):.2f} GB")
        print(f"[green]Usage Percentage:[/green] {mem.percent}%")
    except Exception as e:
        print(f"[bold red]Error fetching RAM info:[/bold red] {e}")
