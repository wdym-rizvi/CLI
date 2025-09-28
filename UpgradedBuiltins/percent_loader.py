import sys
import time

def percent_loader(duration, color=None, bg_color=None):
    """
    CLI percent loader with named colors + 0–255 support
    for both foreground and background.

    Args:
        duration (float): total time in seconds for loader.
        color (str|int|None): text (foreground) color.
        bg_color (str|int|None): background color.
    """

    NAMED = {
        # Standard
        "black": 30, "red": 31, "green": 32, "yellow": 33,
        "blue": 34, "magenta": 35, "cyan": 36, "white": 37,
        # Bright
        "bright_black": 90, "bright_red": 91, "bright_green": 92,
        "bright_yellow": 93, "bright_blue": 94,
        "bright_magenta": 95, "bright_cyan": 96, "bright_white": 97
    }

    def ansi_code(c, is_bg=False):
        if c is None:
            return ""
        if isinstance(c, int):
            if 0 <= c <= 255:
                return f"\x1b[{48 if is_bg else 38};5;{c}m"
            raise ValueError("Integer color must be 0–255")
        if isinstance(c, str):
            key = c.lower()
            if key in NAMED:
                base = NAMED[key]
                if is_bg:
                    base += 10  # switch to background
                return f"\x1b[{base}m"
            raise ValueError(f"Unknown color name: {c}")
        raise TypeError("color must be None, str, or int 0–255")

    RESET = "\x1b[0m"
    fg = ansi_code(color, False)
    bg = ansi_code(bg_color, True)
    color_pre = fg + bg

    steps = 50
    try:
        for i in range(steps + 1):
            percent = i * 100 // steps
            bar = "#" * i + "-" * (steps - i)
            if color_pre:
                colored = f"{color_pre}{bar} {percent}%{RESET}"
            else:
                colored = f"{bar} {percent}%"
            sys.stdout.write(f"\r[{colored}]")
            sys.stdout.flush()
            time.sleep(duration / steps)
    finally:
        sys.stdout.write(RESET + "\n")
        sys.stdout.flush()
