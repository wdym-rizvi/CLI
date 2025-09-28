import sys
import time

def progress(total: int = 50, delay: float = 0.05, 
             char_complete: str = "█", char_incomplete: str = "-", 
             color: str = "\033[92m", reset: str = "\033[0m"):
    """
    Display a progress bar in the terminal.

    Args:
        total (int): Number of steps (length of the bar).
        delay (float): Delay (in seconds) between updates.
        char_complete (str): Character for completed portion.
        char_incomplete (str): Character for incomplete portion.
        color (str): ANSI escape color code for bar text.
        reset (str): ANSI escape reset code.

    Example:
        progress(total=30, delay=0.1)
        progress(total=40, char_complete='#', color="\033[94m")
    """
    for i in range(total + 1):
        bar = char_complete * i + char_incomplete * (total - i)
        percent = i * 100 // total
        sys.stdout.write(f"\r{color}[{bar}] {percent}%{reset}")
        sys.stdout.flush()
        time.sleep(delay)
    print()
