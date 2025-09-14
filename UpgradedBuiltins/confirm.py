def confirm(question: str, default: bool | None = None) -> bool:
    """
    Ask the user a yes/no question until a valid answer is given.

    Args:
        question (str): The question to ask the user.
        default (bool | None): The default answer if the user just presses Enter.
            - True for 'yes'
            - False for 'no'
            - None for no default (forces explicit input)

    Returns:
        bool: True if the user confirms, False otherwise.
    """
    while True:
        if default is True:
            prompt = " (Y/n): "
        elif default is False:
            prompt = " (y/N): "
        else:
            prompt = " (y/n): "

        ans = input(f"{question}{prompt}").strip().lower()

        if not ans and default is not None:
            return default
        if ans in ("y", "yes"):
            return True
        if ans in ("n", "no"):
            return False
