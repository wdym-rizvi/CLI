# Functions/traceroute.py
"""
Runs system traceroute (tracert on Windows, traceroute on Unix).
Uses subprocess so output is readable.
"""
from rich import print
import subprocess
import platform

def run():
    print("[bold cyan]Traceroute[/bold cyan]")
    host = input("Host/IP: ").strip()
    if not host:
        print("[yellow]No host provided.[/yellow]"); return
    cmd = ["tracert", host] if platform.system().lower().startswith("win") else ["traceroute", host]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        print(proc.stdout or proc.stderr)
    except subprocess.TimeoutExpired:
        print("[red]Traceroute timed out.[/red]")
    except Exception as e:
        print(f"[red]Error running traceroute:[/red] {e}")
