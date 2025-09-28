# Functions/zip_folder.py
"""
Zip a folder into a .zip archive.
"""
from rich import print
import zipfile, os

def run():
    print("[bold cyan]Zip Folder Utility[/bold cyan]")
    folder = input("Folder path to zip: ").strip()
    if not folder or not os.path.isdir(folder):
        print("[red]Invalid folder.[/red]"); return
    out = input("Output zip filename (default foldername.zip): ").strip() or (os.path.basename(folder.rstrip("\\/")) + ".zip")
    try:
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
            for root, dirs, files in os.walk(folder):
                for f in files:
                    full = os.path.join(root, f)
                    arc = os.path.relpath(full, start=os.path.dirname(folder))
                    z.write(full, arc)
        print(f"[green]Zipped to {out}[/green]")
    except Exception as e:
        print(f"[red]Zip error:[/red] {e}")
