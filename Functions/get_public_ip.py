# get_ip.py
try:
    import requests
except ImportError:
    print("requests module not found. Installing...")
    import os
    os.system("pip install requests")
    import requests

from time import sleep

from UpgradedBuiltins import typewrite

def run():
    typewrite("Fetching your public IP...", "Bold Cyan", 0.05)
    try:
        ip = requests.get("https://api64.ipify.org?format=json", timeout=5).json()["ip"]
        typewrite(f"Your Public IP: {ip}", "Bold Green", 0.05)
        sleep(1.5)
    except Exception as e:
        typewrite(f"Error getting IP: {e}", "Bold Red", 0.05)
        sleep(1.5)

