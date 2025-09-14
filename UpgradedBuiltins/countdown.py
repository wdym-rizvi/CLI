import time
def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"\r⏳ {i} sec left", end="")
        time.sleep(1)
    print("\n🚀 Time’s up!")
