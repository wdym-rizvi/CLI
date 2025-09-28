# Functions/whois_lookup.py
"""
WHOIS lookup (uses python-whois).
Requires: python-whois (pip install python-whois)
"""
from rich import print
try:
    import whois
except ImportError:
    print("[red]python-whois module not found. Installing...[/red]")
    import os
    os.system("pip install python-whois")
    import whois


def run():
    print("[bold cyan]WHOIS Lookup[/bold cyan]")
    domain = input("Domain (example.com): ").strip()
    if not domain:
        print("[yellow]No domain provided.[/yellow]")
        return
    try:
        w = whois.whois(domain)
        # Print selected fields
        for key in ("domain_name", "registrar", "creation_date", "expiration_date", "name_servers", "emails"):
            val = w.get(key)
            print(f"[green]{key}:[/green] {val}")
    except Exception as e:
        print(f"[red]WHOIS error:[/red] {e}")
