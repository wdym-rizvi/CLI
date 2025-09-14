import sys
import time

def spinner(seconds: int = 3, delay: float = 0.1, chars: str = "|/-\\", color: str = "\033[92m"):
    """
    Display a spinner animation in the terminal.

    Args:
        seconds (int): Duration of the spinner in seconds.
        delay (float): Delay (in seconds) between spinner updates.
        chars (str): Characters used for the spinner animation.
        color (str): ANSI color code for the spinner.

    Example:
        spinner(5)  
        spinner(3, delay=0.05, chars="◐◓◑◒", color="\033[96m")
    """
    end = time.time() + seconds
    i = 0
    while time.time() < end:
        sys.stdout.write(f"\r{color}{chars[i % len(chars)]}\033[0m")
        sys.stdout.flush()
        time.sleep(delay)
        i += 1
    print("\rDone!     ")
