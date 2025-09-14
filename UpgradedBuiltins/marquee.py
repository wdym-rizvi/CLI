import time
from rich.console import Console

console = Console()

def marquee(text: str, repeat: int = 3, delay: float = 0.1, color: str = "cyan"):
    """
    Display a scrolling marquee animation in the terminal.

    Args:
        text (str): The text to scroll.
        repeat (int): How many times the scrolling effect should repeat.
        delay (float): Delay (in seconds) between frames.
        color (str): Rich color style for the scrolling text.

    Example:
        marquee("Hello World!", repeat=2, delay=0.05, color="yellow")
    """
    padding = " " * 20
    s = padding + text + padding  # Add padding on both sides
    width = 20  # visible window size

    for _ in range(repeat):
        for i in range(len(s) - width + 1):
            console.print(s[i:i+width], style=color, end="\r", highlight=False)
            time.sleep(delay)
    print()  # Move to next line after finishing
