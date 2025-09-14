# Convert multiline ASCII art string into list of lines

def ascii_to_list(ascii_art: str):
    return ascii_art.strip("\n").splitlines()