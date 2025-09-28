# Functions/process_list.py
"""
List running processes and optionally kill by PID (requires permissions).
Uses psutil.
"""
from rich import print
from rich.table import Table
import psutil

def run():
    print("[bold cyan]Process List[/bold cyan]")
    table = Table("PID", "Name", "User", "CPU%", "Memory%")
    for p in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_percent']):
        info = p.info
        table.add_row(str(info['pid']), str(info.get('name')), str(info.get('username')), str(info.get('cpu_percent')), f"{info.get('memory_percent'):.2f}" if info.get('memory_percent') else "0")
    print(table)
    if input("Kill process by PID? (y/N): ").strip().lower() == "y":
        pid = int(input("PID: ").strip())
        try:
            psutil.Process(pid).terminate()
            print("[green]Terminate signal sent.[/green]")
        except Exception as e:
            print(f"[red]Failed to terminate:[/red] {e}")
