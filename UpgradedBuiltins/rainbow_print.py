import sys
def rainbow_print(text):
    colors = ["\033[91m", "\033[93m", "\033[92m", "\033[96m", "\033[94m", "\033[95m"]
    for i, char in enumerate(text):
        sys.stdout.write(colors[i % len(colors)] + char + "\033[0m")
    print()
