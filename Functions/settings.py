# Functions/settings.py

import os
import json
from rich.console import Console
import UpgradedBuiltins as upg

console = Console()

CONFIG_FILE = os.path.join("configs", "config.json")
MUSIC_FILE = os.path.join("configs", "music.json")

def run():
    """
    Settings Menu:
    - Change stored name
    - Enable/disable background music
    """
    upg.clear()
    console.print("\n[bold cyan]=== Settings Menu ===[/bold cyan]")
    console.print("[1] Change Name")
    console.print("[2] Toggle Music On/Off")
    console.print("[0] Back\n")

    choice = input("Select an option: ")

    if choice == "1":
        new_name = upg.inputStr("Enter your new name: ", "Bold Cyan")
        if new_name:
            os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)
            with open(CONFIG_FILE, "w") as f:
                json.dump({"name": new_name}, f, indent=4)
            console.print(f"[green]Name updated to:[/green] {new_name}")
        else:
            console.print("[red]Invalid name, unchanged.[/red]")

    elif choice == "2":
        os.makedirs(os.path.dirname(MUSIC_FILE), exist_ok=True)
        enabled = False
        if os.path.exists(MUSIC_FILE):
            try:
                with open(MUSIC_FILE, "r") as f:
                    data = json.load(f)
                    enabled = data.get("music_enabled", False)
            except:
                pass

        console.print(f"Current music setting: {'ON' if enabled else 'OFF'}")
        toggle = input("Turn music ON? (y/n): ").strip().lower()
        new_setting = True if toggle == "y" else False

        with open(MUSIC_FILE, "w") as f:
            json.dump({"music_enabled": new_setting}, f, indent=4)

        console.print(f"[green]Music setting updated to:[/green] {'ON' if new_setting else 'OFF'}")

    elif choice == "0":
        return
    else:
        console.print("[red]Invalid option![/red]")
