from time import sleep
from rich.console import Console
from rich.text import Text
import sys
import os

console = Console()

def print_rotated_gradient(lines, colors, delay):
    for i, line in enumerate(lines):
        color = colors[i % len(colors)]
        text = Text(line, style=color)
        console.print(text)
        sleep(delay)


