from time import sleep
from rich.console import Console
import sys

# Initialize Rich Console
console = Console()

# Error message for invalid input
ERROR_STR = "Enter a valid String: "

def inputStr(prompt: str, color: str = "cyan", delay: float = 0.05) -> str:
    """
    Prompt the user for a string input with animated colored text.

    Args:
        prompt (str): The message to display before user input.
        color (str): Rich color style for the prompt text.
        delay (float): Delay between printing each character (for animation).

    Returns:
        str: The string entered by the user.

    Example:
        name = inputStr("Enter your name: ", color="green", delay=0.03)
        print(f"Hello, {name}!")
    """
    # Print prompt with animation
    for char in prompt:
        console.print(char, style=color, end="", highlight=False)
        sleep(delay)
    sys.stdout.flush()

    # Loop until valid input is received
    while True:
        try:
            str_ = input()  # Take input from user
            break
        except:
            for char in ERROR_STR:
                console.print(char, style="Red", end="", highlight=False)
                sleep(delay)

    return str_  # Return the input string
