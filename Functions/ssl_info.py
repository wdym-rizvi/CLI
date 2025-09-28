# Functions/ssl_info.py
"""
Fetch SSL certificate information (expiry date).
"""
from rich import print
import ssl, socket
from datetime import datetime

def run():
    print("[bold cyan]SSL Certificate Info[/bold cyan]")
    host = input("Host (example.com): ").strip()
    port = int(input("Port (default 443): ") or 443)
    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=host) as s:
            s.settimeout(5)
            s.connect((host, port))
            cert = s.getpeercert()
        # parse notAfter
        not_after = cert.get("notAfter")
        expires = datetime.strptime(not_after, "%b %d %H:%M:%S %Y %Z")
        days_left = (expires - datetime.utcnow()).days
        print(f"[green]Issuer:[/green] {cert.get('issuer')}")
        print(f"[green]Subject:[/green] {cert.get('subject')}")
        print(f"[green]Expires on:[/green] {expires} (in {days_left} days)")
    except Exception as e:
        print(f"[red]Error fetching certificate:[/red] {e}")
