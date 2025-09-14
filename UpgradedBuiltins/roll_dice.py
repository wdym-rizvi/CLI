import random

def roll_dice(sides: int = 6, rolls: int = 1) -> list[int]:
    """
    Roll a dice (or multiple dice) and return the result(s).

    Args:
        sides (int): Number of sides on the dice (default=6).
        rolls (int): Number of times to roll the dice.

    Returns:
        list[int]: List of roll results.

    Example:
        roll_dice()          # -> [4]
        roll_dice(20)        # -> [17]
        roll_dice(6, rolls=3) # -> [2, 5, 1]
    """
    return [random.randint(1, sides) for _ in range(rolls)]
