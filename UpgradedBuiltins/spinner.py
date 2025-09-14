import sys, time
def spinner(seconds):
    chars = "|/-\\"
    end = time.time() + seconds
    i = 0
    while time.time() < end:
        sys.stdout.write("\r" + chars[i % 4])
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    print("\rDone!")
