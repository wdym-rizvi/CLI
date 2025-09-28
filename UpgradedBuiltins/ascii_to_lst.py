# Convert multiline ASCII art string into list of lines

def ascii_to_list(ascii_art: str):
    """
    Convert a multiline ASCII art string into a list of lines.

    Args:
        ascii_art (str): ASCII art in a single multiline string.

    Returns:
        list[str]: list where each element is one line of the ASCII art.

    Usage:
        art = '''
        ####
        #  #
        ####
        '''
        lines = ascii_to_list(art)
        print(lines)
        # Output: ['####', '#  #', '####']
    """
    return ascii_art.strip("\n").splitlines()
