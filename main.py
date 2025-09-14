#-------------------------------------------------------------------------------
# CLI APP - A Command Line Interface Application
# Version: 1.0
# Coded by Rizvi
# main.py
#--------------------------------------------------------------------------------

# Importing Libraries (Internal)
import UpgradedBuiltins as upg
import os
import json
from rich.console import Console
from time import sleep
import Functions.get_public_ip as option01
import Functions.get_local_ip as option02
import Functions.system_info as option03
import Functions.cpu_usage as option04
import Functions.ram_info as option05
import Functions.screenshot as option06
import Functions.website_screenshot as option07
import Functions.hostname as option08
import Functions.current_time as option09
import Functions.port_scan as option10
import Functions.ssl_info as option11
import Functions.kill_process as option12
import Functions.traceroute as option13
import Functions.dns_lookup as option14
import Functions.whois_lookup as option15
import Functions.zip_folder as option16
import random, time
#-------------------------------------------------------------------------------
#External Libraries Check and Install
#-------------------------------------------------------------------------------

# Check and install rich if not present
try:
    from rich.console import Console
    from rich.text import Text
except ImportError:
    print("rich module not found. Installing...")
    os.system("pip install rich")
    from rich.console import Console

# Check and install pygame if not present
try:
    import pygame
except ImportError:
    upg.typewrite("pygame module not found. Installing...", "Red", 0.05)
    os.system("pip install pygame")
    import pygame

#-------------------------------------------------------------------------------

# Initialize console
console = Console()

#-------------------------------------------------------------------------------
# Functions
#-------------------------------------------------------------------------------

# Mapping numbers to functions
menu_actions = {
    1: option01.run,
    2: option02.run,
    3: option03.run,
    4: option04.run,
    5: option05.run,
    6: option06.run,
    7: option07.run,
    8: option08.run,
    9: option09.run,
    10: option10.run,
    11: option11.run,
    12: option12.run,
    13: option13.run,
    14: option14.run,
    15: option15.run,
    16: option16.run,
    99: lambda: console.print("CLI APP Version 1.0\nCoded by Rizvi\nAll rights reserved © 2025", style="bold cyan"),
}

# Function to play sound in a separate thread
def play_sound(sound):
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(sound)  # can also be .mp3
        pygame.mixer.music.play()
    except Exception as e:
        print("Sound failed:", e)


# Function to simulate a fake boot sequence

def fake_boot_sequence():
    logs = [
        "Initializing core modules...",
        "Importing UpgradedBuiltins...",
        "Loaded config.json successfully",
        "Checking environment variables...",
        "Added registry keys...",
        "Importing rich.console...",
        "Loading Functions package...",
        "Memory mapping completed",
        "Establishing secure channel...",
        "System entropy pool updated",
        "Optimizing runtime performance...",
        "Patching I/O buffer...",
        "Verifying digital signatures...",
        "Mounted virtual disk...",
        "Fetching remote resources...",
        "Encrypting temporary cache...",
        "Registry entries updated",
        "Allocating virtual memory...",
        "Loading ASCII art renderer...",
        "CLI environment ready",
    ]

    for i in range(2000):  # print 2000 fake lines
        msg = random.choice(logs)
        style = random.choice(["bold Red", "dark_green"])
        console.print(f"[{style}] [BOOT] {msg}")
        time.sleep(0.0005)  # small random delay

#-------------------------------------------------------------------------------

# Clear the console at the start
upg.clear()
#-------------------------------------------------------------------------------
# Startup
#-------------------------------------------------------------------------------

# Play a system sound when program starts
play_sound("startup.wav")

# Initial Message
upg.typewrite("Starting CLI APP...", "Bold Green", 0.1)

sleep(2.5)  # Wait for 2 seconds to let the sound play
fake_boot_sequence()  # Simulate boot sequence
sleep(1)  # Pause before clearing the consoles
# Clear console again
upg.clear()

#-------------------------------------------------------------------------------

#Printing Banner
ls= upg.ascii_to_list('''
$$\      $$\           $$\                                             
$$ | $\  $$ |          $$ |                                            
$$ |$$$\ $$ | $$$$$$\  $$ | $$$$$$$\  $$$$$$\  $$$$$$\$$$$\   $$$$$$\  
$$ $$ $$\$$ |$$  __$$\ $$ |$$  _____|$$  __$$\ $$  _$$  _$$\ $$  __$$\ 
$$$$  _$$$$ |$$$$$$$$ |$$ |$$ /      $$ /  $$ |$$ / $$ / $$ |$$$$$$$$ |
$$$  / \$$$ |$$   ____|$$ |$$ |      $$ |  $$ |$$ | $$ | $$ |$$   ____|
$$  /   \$$ |\$$$$$$$\ $$ |\$$$$$$$\ \$$$$$$  |$$ | $$ | $$ |\$$$$$$$\ 
\__/     \__| \_______|\__| \_______| \______/ \__| \__| \__| \_______|
                                                         Coded By Rizvi
                                                            Version 1.0''')

upg.print_rotated_gradient(ls, ["Red", "Yellow"],0.05)

#-------------------------------------------------------------------------------

# Welcome Message
upg.typewrite("Welcome to CLI APP", "Red", 0.1)

print()


# Check if program is run for the first time or config.json is empty

config_file = "config.json"

# Check if config.json exists and is not empty
if not os.path.exists(config_file) or os.stat(config_file).st_size == 0:
    # Ask for name first time
    x = upg.inputStr("Enter your name: ", "Yellow", 0.1)
    # Save into JSON
    with open(config_file, "w") as f:
        json.dump({"name": x}, f, indent=4)
else:
    # Load existing name
    with open(config_file, "r") as f:
        data = json.load(f)
        x = data["name"]

upg.marquee(f"Hello, {x}!", 1, 0.1, "Cyan") # Greet the user
print() # New line for better readability

while True:
    upg.clear() # Clear the console


    # Main Menu

    # Main Menu Banner
    lst = upg.ascii_to_list('''
    $$$$$$\  $$\       $$$$$$\ 
    $$  __$$\ $$ |      \_$$  _|
    $$ /  \__|$$ |        $$ |  
    $$ |      $$ |        $$ |  
    $$ |      $$ |        $$ |  
    $$ |  $$\ $$ |        $$ |  
    \$$$$$$  |$$$$$$$$\ $$$$$$\ 
    \______/ \________|\______|
                Coded By Rizvi
                    Version 1.0''')


    upg.print_rotated_gradient(lst, ["Blue", "Green"],0.05)
    #-------------------------------------------------------

    print() # New line for better readability

    # Menu Options


    console.print("[cyan][01][/cyan] Public IP           [cyan][09][/cyan] Current Time")
    console.print("[cyan][02][/cyan] Local IP            [cyan][10][/cyan] Port Scan")
    console.print("[cyan][03][/cyan] System Info         [cyan][11][/cyan] SSL Info")
    console.print("[cyan][04][/cyan] CPU Usage           [cyan][12][/cyan] Kill Process")
    console.print("[cyan][05][/cyan] RAM Info            [cyan][13][/cyan] Traceroute")
    console.print("[cyan][06][/cyan] Screenshot          [cyan][14][/cyan] DNS Lookup")
    console.print("[cyan][07][/cyan] Website Screenshot  [cyan][15][/cyan] WHOIS Lookup")
    console.print("[cyan][08][/cyan] Hostname            [cyan][16][/cyan] Zip Folder")

    console.print("\n[yellow][99][/yellow] About         [yellow][00][/yellow] Exit\n")


    # Getting choice and calling functions accordingly
    choice = upg.inputInt("Select an option : ", "yellow", 0.1)
    console.print(f"You selected: {choice}", style="green")
    sleep(1)  # Pause for a moment to let user see their choice

    # Exit if 0 is chosen
    if choice == 0:
        upg.typewrite("Exiting... Goodbye!", "Red", 0.1)
        break
    else:
        # Run the function if valid, else warn
        action = menu_actions.get(choice)
        if action:
            action()
            upg.inputStr("Press any key to return to the main menu...", "Yellow", 0.03)
        else:
            console.print("Invalid option, try again!", style="red")
            sleep(1.5)  # Pause before re-displaying the menu
        
