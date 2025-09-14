from time import sleep
from rich.console import Console
from rich.text import Text
import sys
import os

# Initialize Rich Console
console = Console()

# Error message for invalid input
error_str="Enter a valid String: "

# Function to get string input with animated prompt
def inputStr(prompt: str, color: str, delay: float):
    for char in prompt:
        console.print(char, style=color, end="", highlight=False)
        sleep(delay)
    sys.stdout.flush()
    # Loop until valid input is received
    while True:
        try:
            str_ = input() # Take input from user
            break
        except:
            for char in error_str:
                console.print(char, style="Red", end="", highlight=False)
                sleep(delay)
    return str_ # Return the input string