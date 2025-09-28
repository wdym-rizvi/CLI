import sys

def rainbow_print(text: str, colors: list[str] = None):
    """
    Print text with rainbow coloring (cycling through ANSI colors).

    Args:
        text (str): The text to print with rainbow colors.
        colors (list[str], optional): List of ANSI color codes to cycle through.
                                      Defaults to a rainbow sequence.

    Example:
        rainbow_print("Hello World!")
    """
    if colors is None:
        colors = [
            "\033[91m",  # Red
            "\033[93m",  # Yellow
            "\033[92m",  # Green
            "\033[96m",  # Cyan
            "\033[94m",  # Blue
            "\033[95m",  # Magenta
        ]

    for i, char in enumerate(text):
        sys.stdout.write(colors[i % len(colors)] + char + "\033[0m")
    print()
