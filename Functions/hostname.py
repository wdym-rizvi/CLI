from rich import print
import socket

def run():
    print("[bold cyan]Fetching hostname and local IP...[/bold cyan]")
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        print(f"[green]Hostname:[/green] {hostname}")
        print(f"[green]Local IP:[/green] {ip}")
    except Exception as e:
        print(f"[bold red]Error fetching hostname:[/bold red] {e}")
