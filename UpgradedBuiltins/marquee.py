import time
from rich.console import Console

console = Console()

def marquee(text, repeat=3, delay=0.1, color="cyan"):
    s = " " * 20 + text + " " * 20
    for _ in range(repeat):
        for i in range(len(s)):
            # Clear line by overwriting with spaces
            console.print(s[i:i+20], style=color, end="\r")
            time.sleep(delay)