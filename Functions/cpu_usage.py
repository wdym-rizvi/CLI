from rich import print
import psutil, time

def run():
    print("[bold cyan]Monitoring CPU usage (5 seconds)...[/bold cyan]")
    try:
        for i in range(5):
            usage = psutil.cpu_percent(interval=1)
            print(f"[green]CPU Usage:[/green] {usage}%")
    except Exception as e:
        print(f"[bold red]Error checking CPU usage:[/bold red] {e}")
