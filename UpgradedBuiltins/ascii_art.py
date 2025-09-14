from time import sleep
from rich.console import Console
from rich.text import Text

console = Console()

def print_rotated_gradient(lines, colors, delay):
    """
    Print multiple lines with rotating gradient colors.

    Args:
        lines (list[str]): list of text lines to print.
        colors (list[str]): list of color names/hex codes understood by Rich 
                            (e.g., ["red", "green", "#00ffcc"]).
        delay (float): delay in seconds between printing each line.

    Usage:
        lines = ["Hello", "World", "Gradient!"]
        colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]
        print_rotated_gradient(lines, colors, 0.2)
    """
    for i, line in enumerate(lines):
        color = colors[i % len(colors)]  # cycle through colors
        text = Text(line, style=color)
        console.print(text)
        sleep(delay)
