try:
    from rich import print
except ImportError:
    print("rich module not found. Installing...")
    import os
    os.system("pip install rich")
try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
except ImportError:
    print("selenium module not found. Installing...")
    import os
    os.system("pip install selenium")
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

from UpgradedBuiltins import inputStr

def run():
    url = inputStr("Enter the website URL (including http/https): ", "Yellow", 0.03)
    filename = "website.png"
    print(f"[bold cyan]Capturing screenshot of {url}...[/bold cyan]")
    try:
        options = Options() # Set Chrome options
        options.add_argument("--headless") # Run in headless mode to avoid opening a browser window
        options.add_argument("--disable-gpu") # Disable GPU acceleration
        driver = webdriver.Chrome(options=options) # Initialize Chrome WebDriver
        driver.set_window_size(1920, 1080) # Set window size to ensure full page is captured
        driver.get(url) # Navigate to the URL
        driver.save_screenshot(filename) # Save screenshot
        driver.quit() # Close the browser
        print(f"[bold green]Website screenshot saved as {filename}[/bold green]")
    except Exception as e:
        print(f"[bold red]Error taking website screenshot:[/bold red] {e}")
