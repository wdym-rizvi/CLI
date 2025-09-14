# Functions/dns_lookup.py
"""
Simple DNS lookup (A, AAAA, MX).
Requires: dnspython (pip install dnspython)
"""
from rich import print
try:
    import dns.resolver
except ImportError:
    print("[red]dnspython module not found. Installing...[/red]")
    import os
    os.system("pip install dnspython")
    import dns.resolver

def run():
    print("[bold cyan]DNS Lookup Utility[/bold cyan]")
    try:
        domain = input("Domain (example.com): ").strip()
        if not domain:
            print("[yellow]No domain provided. Aborting.[/yellow]")
            return

        resolver = dns.resolver.Resolver()
        for rtype in ("A", "AAAA", "MX"):
            try:
                answers = resolver.resolve(domain, rtype, lifetime=5)
                print(f"[green]{rtype} records:[/green]")
                for r in answers:
                    print(f"  - {r.to_text()}")
            except Exception as e:
                print(f"[magenta]{rtype}:[/magenta] [red]No records or error ({e})[/red]")
    except Exception as e:
        print(f"[red]Unexpected error:[/red] {e}")
