import sys, time
def progress(total, delay):
    for i in range(total+1):
        bar = "█"*i + "-"*(total-i)
        sys.stdout.write(f"\r[{bar}] {i*100//total}%")
        sys.stdout.flush()
        time.sleep(delay)
    print()
