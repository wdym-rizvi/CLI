import time

def countdown(seconds: int, message: str = "🚀 Time’s up!"):
    """
    Display a countdown timer in the terminal.

    Args:
        seconds (int): Number of seconds to count down.
        message (str): Message to display when the countdown ends.

    Example:
        countdown(5)  
        countdown(10, "🎉 Done!")  
    """
    for i in range(seconds, 0, -1):
        print(f"\r⏳ {i} sec left", end="")
        time.sleep(1)
    print(f"\n{message}")
