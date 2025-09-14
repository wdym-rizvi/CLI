def confirm(question: str) -> bool:
    while True:
        ans = input(f"{question} (y/n): ").lower().strip()
        if ans in ("y", "yes"): return True
        if ans in ("n", "no"): return False
