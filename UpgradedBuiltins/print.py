from time import sleep
from rich.console import Console
import sys

console = Console()

def typewrite(text: str, color: str = "cyan", delay: float = 0.05):
    """
    Print text with a typewriter animation effect.

    Args:
        text (str): The text to display.
        color (str): Rich color style for the text.
        delay (float): Delay (in seconds) between each character.

    Example:
        typewrite("Hello, World!", color="green", delay=0.1)
    """
    for char in text:
        console.print(char, style=color, end="", highlight=False)
        sleep(delay)
    sys.stdout.flush()
    print()  # Ensure the cursor moves to the next line
