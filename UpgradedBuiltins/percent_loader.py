import sys, time
def percent_loader(duration):
    steps = 50
    for i in range(steps+1):
        percent = i*100//steps
        bar = "#"*i + "-"*(steps-i)
        sys.stdout.write(f"\r[{bar}] {percent}%")
        sys.stdout.flush()
        time.sleep(duration/steps)
    print()
