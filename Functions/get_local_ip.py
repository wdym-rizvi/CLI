import socket
from UpgradedBuiltins import typewrite
from time import sleep
def run():
    """Return the machine's local IP"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        typewrite(f"Local IP: {ip}", "Bold Green", 0.05)
        sleep(1.5)
    except Exception as e:
        typewrite(f"Failed to get local IP: {e}", "Bold Red", 0.05)
        sleep(1.5)