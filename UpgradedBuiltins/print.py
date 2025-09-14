from time import sleep
from rich.console import Console
from rich.text import Text
import sys
import os

console = Console()

def typewrite(text: str, color: str, delay: float):
    for char in text:
        console.print(char, style=color, end="", highlight=False)
        sleep(delay)
    sys.stdout.flush()
    print()
