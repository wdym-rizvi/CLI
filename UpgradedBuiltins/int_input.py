from time import sleep
from rich.console import Console
from rich.text import Text
import sys
import os

# Initialize Rich Console
console = Console()

# Error message for invalid input
error="Enter a valid Number: "

# Function to get integer input with animated prompt
def inputInt(prompt: str, color: str, delay: float):
    for char in prompt:
        console.print(char, style=color, end="", highlight=False)
        sleep(delay)
    sys.stdout.flush()
    # Loop until valid input is received
    while True:
        try:
            int_ = int(input()) # Take input from user and convert to int
            break
        except:
            for char in error:
                console.print(char, style="Red", end="", highlight=False)
                sleep(delay)
    return int_ # Return the input integer