# run.py
# The main Login and redirect system
# Version: 1.2
# Coded by Rizvi

#------------------------------------------------------
# Internal Libraries
#------------------------------------------------------
import json
import os
import time
import sys
import threading
import platform
from app import run  # import run() from app.py
import UpgradedBuiltins as upg

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
    pass

#------------------------------------------------------
# Load key + credentials
#------------------------------------------------------
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

#------------------------------------------------------
# Timer / UI globals
#------------------------------------------------------
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

#------------------------------------------------------
# Cross-platform non-blocking input
#------------------------------------------------------
if os.name == "nt":
    import msvcrt

    def input_with_timeout(prompt, timeout=0.1):
        sys.stdout.write(prompt)
        sys.stdout.flush()
        input_str = ""
        while not stop_event.is_set():
            if msvcrt.kbhit():
                char = msvcrt.getwch()
                if char == "\r":  # Enter
                    print()
                    return input_str
                elif char == "\b":
                    if input_str:
                        input_str = input_str[:-1]
                        sys.stdout.write("\b \b")
                else:
                    input_str += char
                    sys.stdout.write(char)
                sys.stdout.flush()
            time.sleep(timeout)
        print()
        return None

else:
    import select

    def input_with_timeout(prompt, timeout=0.1):
        sys.stdout.write(prompt)
        sys.stdout.flush()
        input_str = ""
        while not stop_event.is_set():
            ready, _, _ = select.select([sys.stdin], [], [], timeout)
            if ready:
                line = sys.stdin.readline()
                return line.strip()
        print()
        return None

#------------------------------------------------------
# Timer functions
#------------------------------------------------------
def clear_timer_line():
    """Clear the top timer line."""
    sys.stdout.write(SAVE_CURSOR + CURSOR_TOP_LEFT + ERASE_LINE + RESTORE_CURSOR)
    sys.stdout.flush()

def countdown():
    """Update timer on the top line without disturbing user input."""
    global time_left
    while time_left > 0 and not stop_event.is_set():
        mins, secs = divmod(time_left, 60)
        timer_display = f"⏳ Time left: {mins:02d}:{secs:02d}"

        sys.stdout.write(SAVE_CURSOR + CURSOR_TOP_LEFT + ERASE_LINE + MAGENTA + timer_display + RESET + RESTORE_CURSOR)
        sys.stdout.flush()

        time.sleep(1)
        time_left -= 1

    if not stop_event.is_set():
        clear_timer_line()
        sys.stdout.write(MAGENTA + "⏳ Time left: 00:00" + RESET + "\n")
        sys.stdout.flush()
        upg.typewrite("⏰ Time over! Exiting...", "red", 0.05)
        stop_event.set()
        sys.exit(1)

#------------------------------------------------------
# Login function
#------------------------------------------------------
def login():
    global time_left

    upg.clear()
    print()  # reserve top line for timer
    upg.typewrite("Welcome to the System", "cyan", 0.05)
    upg.typewrite("Please log in to continue", "cyan", 0.05)

    t = threading.Thread(target=countdown, daemon=True)
    t.start()

    attempts = 3
    while attempts > 0 and not stop_event.is_set():
        username = input_with_timeout("Enter Username: ")
        if username is None:
            stop_event.set()
            break

        password = input_with_timeout("Enter Password: ")
        if password is None:
            stop_event.set()
            break

        if username == USERNAME and password == PASSWORD:
            stop_event.set()
            clear_timer_line()
            upg.typewrite("✅ Login successful! Redirecting...", "green", 0.05)
            time.sleep(0.5)
            return True
        else:
            attempts -= 1
            upg.typewrite(f"❌ Invalid credentials. {attempts} attempts left.", "red", 0.05)

    stop_event.set()
    clear_timer_line()
    if attempts == 0:
        upg.typewrite("Too many failed attempts. Exiting...", "red", 0.05)
    else:
        upg.typewrite("Login aborted or time expired. Exiting...", "red", 0.05)
    sys.exit(1)

#------------------------------------------------------
# Main
#------------------------------------------------------
if __name__ == "__main__":
    success = login()
    if success:
        clear_timer_line()
        try:
            run()
        except Exception as e:
            upg.typewrite("Failed to launch app: " + str(e), "Bold Red")
            sys.exit(1)
        sys.exit(0)
