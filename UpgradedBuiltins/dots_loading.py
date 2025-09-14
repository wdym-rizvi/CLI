import sys, time
def dots_loading(text, dots, delay, repeat):
    for _ in range(repeat):
        for i in range(dots+1):
            sys.stdout.write("\r" + text + "."*i + " "*(dots-i))
            sys.stdout.flush()
            time.sleep(delay)
    print()
