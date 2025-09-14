import sys
import time

def percent_loader(duration, color=None):
    """
    Show a CLI percent loader with optional color for the bar.

    Args:
        duration (float): total time in seconds for the loader to complete.
        color (str|int|None): color name (e.g. "red", "green") or
                              an integer 0-255 for ANSI 256 colors.
                              None = no color.
    """
    # Named 8/16-color map (foreground codes)
    NAMED = {
        "black": 30, "red": 31, "green": 32, "yellow": 33,
        "blue": 34, "magenta": 35, "cyan": 36, "white": 37,
        "bright_black": 90, "bright_red": 91, "bright_green": 92,
        "bright_yellow": 93, "bright_blue": 94, "bright_magenta": 95,
        "bright_cyan": 96, "bright_white": 97
    }

    def ansi_prefix(c):
        # Accept named colors or 0-255 integer for 256-color mode
        if c is None:
            return ""
        if isinstance(c, int):
            if 0 <= c <= 255:
                return f"\x1b[38;5;{c}m"  # 256-color foreground
            raise ValueError("Integer color must be in range 0-255")
        if isinstance(c, str):
            key = c.lower()
            if key in NAMED:
                return f"\x1b[{NAMED[key]}m"
            # allow "fg<number>" or direct "38;5;nnn" style
            if key.startswith("38;5;"):
                return f"\x1b[{key}m"
            raise ValueError(f"Unknown color name: {c}")
        raise TypeError("color must be None, a string name, or int 0-255")

    RESET = "\x1b[0m"
    color_pre = ansi_prefix(color)
    steps = 50
    try:
        for i in range(steps + 1):
            percent = i * 100 // steps
            bar = "#" * i + "-" * (steps - i)
            # apply color only to the bar, leave percent and brackets default
            if color_pre:
                colored_bar = f"{color_pre}{bar}{RESET}"
            else:
                colored_bar = bar
            sys.stdout.write(f"\r[{colored_bar}] {percent}%")
            sys.stdout.flush()
            time.sleep(duration / steps)
    finally:
        # ensure terminal colors are reset and newline is printed
        sys.stdout.write(RESET + "\n")
        sys.stdout.flush()

