import random, time

def matrix_rain(rows=10, cols=30, duration=3):
    charset = "01"
    green = "\033[92m"   # Bright Green ANSI code
    reset = "\033[0m"    # Reset color
    end = time.time() + duration
    
    while time.time() < end:
        line = "".join(random.choice(charset) for _ in range(cols))
        print(green + line + reset)
        time.sleep(0.1)

