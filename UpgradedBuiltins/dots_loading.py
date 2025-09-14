import sys
import time

def dots_loading(text: str = "Loading", dots: int = 3, delay: float = 0.3, repeat: int = 3):
    """
    Display a simple dots loading animation in the terminal.

    Args:
        text (str): The text shown before the dots.
        dots (int): Maximum number of dots to animate.
        delay (float): Delay (in seconds) between each frame.
        repeat (int): Number of times the animation should repeat.

    Example:
        dots_loading("Processing", dots=5, delay=0.2, repeat=2)
    """
    for _ in range(repeat):
        for i in range(dots + 1):
            sys.stdout.write("\r" + text + "." * i + " " * (dots - i))
            sys.stdout.flush()
            time.sleep(delay)
    print()  # Move to next line after finishing
