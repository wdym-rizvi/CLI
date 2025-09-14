try:
    from rich import print
except ImportError:
    print("rich module not found. Installing...")
    import os
    os.system("pip install rich")
try:
    import pyautogui
except ImportError:
    print("[bold red]pyautogui not found. Installing...[/bold red]")
    os.system("pip install pyautogui")
    import pyautogui
    
import os

def run():
    filename = "screenshot.png"
    print("[bold cyan]Taking screenshot...[/bold cyan]")
    try:
        img = pyautogui.screenshot()
        img.save(filename)
        print(f"[bold green]Screenshot saved as:[/bold green] {filename}")
    except Exception as e:
        print(f"[bold red]Error taking screenshot:[/bold red] {e}")
