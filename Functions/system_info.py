try:
    from rich import print
except ImportError:
    print("rich module not found. Installing...")
    import os
    os.system("pip install rich")
    from rich import print
import platform

def run():
    print("[bold cyan]Fetching system information...[/bold cyan]")
    try:
        print(f"[green]System:[/green] {platform.system()}")
        print(f"[green]Node Name:[/green] {platform.node()}")
        print(f"[green]Release:[/green] {platform.release()}")
        print(f"[green]Version:[/green] {platform.version()}")
        print(f"[green]Machine:[/green] {platform.machine()}")
        print(f"[green]Processor:[/green] {platform.processor()}")
    except Exception as e:
        print(f"[bold red]Error fetching system info:[/bold red] {e}")
