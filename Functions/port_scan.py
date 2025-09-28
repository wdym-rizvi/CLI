# Functions/port_scan.py
"""
Lightweight TCP port scanner (connect-based).
Scans a small range; safe for local and consenting hosts.
"""
from rich import print, progress
import socket
import time

def scan_host(host, start=1, end=1024, timeout=0.3):
    open_ports = []
    for port in range(start, end + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        try:
            if s.connect_ex((host, port)) == 0:
                open_ports.append(port)
        except Exception:
            pass
        finally:
            s.close()
    return open_ports

def run():
    print("[bold cyan]Port Scanner[/bold cyan]")
    host = input("Host (IP or hostname): ").strip()
    if not host:
        print("[yellow]No host given.[/yellow]"); return
    try:
        start = int(input("Start port (default 1): ") or 1)
        end = int(input("End port (default 1024): ") or 1024)
        print(f"[green]Scanning {host} ports {start}-{end} (this may take a bit)...[/green]")
        start_t = time.time()
        open_ports = scan_host(host, start, end)
        elapsed = time.time() - start_t
        if open_ports:
            print(f"[bold green]Open ports:[/bold green] {open_ports}")
        else:
            print("[yellow]No open ports found in range.[/yellow]")
        print(f"[dim]Scan finished in {elapsed:.2f}s[/dim]")
    except ValueError:
        print("[red]Invalid port numbers.[/red]")
    except Exception as e:
        print(f"[red]Error:[/red] {e}")
