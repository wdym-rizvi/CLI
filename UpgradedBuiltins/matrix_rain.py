import random
import time

def matrix_rain(rows: int = 20, cols: int = 60, duration: int = 5, charset: str = "01"):
    """
    Display a Matrix-style digital rain effect in the terminal.

    Args:
        rows (int): Number of lines (height of the rain).
        cols (int): Number of characters per line.
        duration (int): Duration (in seconds) to run the animation.
        charset (str): Characters used for the rain.

    Example:
        matrix_rain(rows=15, cols=40, duration=5, charset="01ABC")
    """
    green = "\033[92m"   # Bright Green ANSI
    reset = "\033[0m"    # Reset color
    end = time.time() + duration

    while time.time() < end:
        # Create random line with occasional blank spaces for variation
        line = "".join(random.choice([random.choice(charset), " "]) for _ in range(cols))
        print(green + line + reset)
        time.sleep(0.05)  # Faster for smoother flow
