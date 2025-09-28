from time import sleep
from rich.console import Console
import sys

# Initialize Rich Console
console = Console()

# Error message for invalid input
ERROR_MSG = "Enter a valid Number: "

def inputInt(prompt: str, color: str = "cyan", delay: float = 0.05) -> int:
    """
    Prompt the user for an integer input with animated colored text.

    Args:
        prompt (str): The message to display before user input.
        color (str): Rich color style for the prompt text.
        delay (float): Delay between printing each character (for animation).

    Returns:
        int: The integer entered by the user.

    Examples:
        number = typewrite("Hello, World!", "Bold Green", 0.1)
    """
    # Print prompt with animation
    for char in prompt:
        console.print(char, style=color, end="", highlight=False)
        sleep(delay)
    sys.stdout.flush()

    # Loop until valid integer input is received
    while True:
        try:
            return int(input())  # Return immediately if valid
        except ValueError:
            # Print error message with animation
            for char in ERROR_MSG:
                console.print(char, style="red", end="", highlight=False)
                sleep(delay)
            sys.stdout.flush()
