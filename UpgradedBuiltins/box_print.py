def box_print(text: str):
    """
    Print text inside a simple ASCII box.

    Args:
        text (str): the text to display inside the box.

    Usage:
        box_print("Hello")
        # Output:
        # +--------+
        # |  Hello  |
        # +--------+
    """
    length = len(text) + 4
    print("+" + "-" * length + "+")
    print("|  " + text + "  |")
    print("+" + "-" * length + "+")
