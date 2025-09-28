# run.py
# The main Login and redirect system
# Version: 1.1
# Coded by Rizvi

#------------------------------------------------------
# Internal Libraries
#------------------------------------------------------
import json
import os
import UpgradedBuiltins as upg
import time
import sys
import threading
from app import run  # import run() from app.py

#------------------------------------------------------
# External Libraries check and install
#------------------------------------------------------
try:
    from cryptography.fernet import Fernet
except ImportError:
    upg.typewrite("cryptography module not found. Installing...", "Bold Red")
    os.system("pip install cryptography")
    from cryptography.fernet import Fernet

# Try to enable ANSI on Windows (best-effort)
try:
    if os.name == "nt":
        import ctypes
        kernel32 = ctypes.windll.kernel32
        handle = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE = -11
        mode = ctypes.c_uint()
        if kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
            ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
            new_mode = mode.value | ENABLE_VIRTUAL_TERMINAL_PROCESSING
            kernel32.SetConsoleMode(handle, new_mode)
except Exception:
    pass  # ignore if not possible

# Load key + credentials
if not os.path.exists("creds/fernet.key") or not os.path.exists("creds/credentials.json"):
    upg.typewrite("Missing fernet.key or credentials.json. Generate credentials first.", "Bold Red")
    sys.exit(1)

with open("creds/fernet.key", "rb") as f:
    key = f.read()
fernet = Fernet(key)

with open("creds/credentials.json", "r", encoding="utf-8") as f:
    data = json.load(f)

try:
    USERNAME = fernet.decrypt(data["username"].encode()).decode()
    PASSWORD = fernet.decrypt(data["password"].encode()).decode()
except Exception as e:
    upg.typewrite("Failed to decrypt credentials: " + str(e), "Bold Red")
    sys.exit(1)

# Timer / UI globals
TIME_LIMIT = 60  # seconds
time_left = TIME_LIMIT
stop_event = threading.Event()

# ANSI codes
MAGENTA = "\033[35m"
RESET = "\033[0m"
SAVE_CURSOR = "\033[s"
RESTORE_CURSOR = "\033[u"
CURSOR_TOP_LEFT = "\033[1;1H"
ERASE_LINE = "\033[2K"

def clear_timer_line():
    """Clear the top timer line (leave cursor where it is)."""
    sys.stdout.write(SAVE_CURSOR + CURSOR_TOP_LEFT + ERASE_LINE + RESTORE_CURSOR)
    sys.stdout.flush()

def countdown():
    """Update timer on the top line without disturbing user input (save/restore)."""
    global time_left
    while time_left > 0 and not stop_event.is_set():
        mins, secs = divmod(time_left, 60)
        timer_display = f"⏳ Time left: {mins:02d}:{secs:02d}"

        # Save cursor, go to top-left, clear that line, print timer, restore cursor
        sys.stdout.write(
            SAVE_CURSOR +
            CURSOR_TOP_LEFT +
            ERASE_LINE +
            MAGENTA + timer_display + RESET +
            RESTORE_CURSOR
        )
        sys.stdout.flush()

        time.sleep(1)
        time_left -= 1

    if not stop_event.is_set():
        # show 00:00 then exit
        sys.stdout.write(
            SAVE_CURSOR +
            CURSOR_TOP_LEFT +
            ERASE_LINE +
            MAGENTA + "⏳ Time left: 00:00" + RESET +
            RESTORE_CURSOR + "\n"
        )
        sys.stdout.flush()
        upg.typewrite("⏰ Time over! Exiting...", "red", 0.05)
        sys.exit(1)

def login():
    """Main login flow. Timer runs in background and is stopped on success/fail."""
    global time_left

    upg.clear()

    # reserve the top line for the timer (so timer prints at line 1)
    print()  # blank first line for timer

    upg.typewrite("Welcome to the System", "cyan", 0.05)
    upg.typewrite("Please log in to continue", "cyan", 0.05)

    # start the countdown thread
    t = threading.Thread(target=countdown, daemon=True)
    t.start()

    attempts = 3
    while attempts > 0 and time_left > 0 and not stop_event.is_set():
        # Prompt appears below the reserved timer line
        username = upg.inputStr("Enter Username: ", "yellow")
        password = upg.inputStr("Enter Password: ", "yellow")

        if username == USERNAME and password == PASSWORD:
            # Stop timer and clear the timer line before printing success
            stop_event.set()
            clear_timer_line()
            upg.typewrite("✅ Login successful! Redirecting...", "green", 0.05)
            time.sleep(0.5)
            return True
        else:
            attempts -= 1
            # show error (timer keeps running above)
            upg.typewrite(f"❌ Invalid credentials. {attempts} attempts left.", "red", 0.05)

    # stop timer and handle exit
    stop_event.set()
    clear_timer_line()
    if attempts == 0:
        upg.typewrite("Too many failed attempts. Exiting...", "red", 0.05)
    else:
        upg.typewrite("Login aborted or time expired. Exiting...", "red", 0.05)
    sys.exit(1)


if __name__ == "__main__":
    success = login()
    if success:
        clear_timer_line()
        try:
            run()  # directly call function
        except Exception as e:
            upg.typewrite("Failed to launch app: " + str(e), "Bold Red")
            sys.exit(1)
        sys.exit(0)
