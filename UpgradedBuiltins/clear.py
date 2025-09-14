import os
import sys

def clear():
    """Clear the terminal screen (cross-platform)."""
    os.system("cls" if sys.platform == "win32" else "clear")
