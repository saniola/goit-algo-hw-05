def build_shift_table(pattern):
    """Build the shift table for the Boyer-Moore algorithm."""
    table = {}
    length = len(pattern)
    # For each character in the pattern, set the shift equal to the length of the pattern
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    # If the character is not in the table, the shift will be equal to the length of the pattern
    table.setdefault(pattern[-1], length)
    return table


def boyer_moore(text, pattern):
    # Build the shift table for the pattern
    shift_table = build_shift_table(pattern)
    i = 0  # Initialize the starting index for the main text

    # Traverse the main text, comparing with the pattern
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1  # Start from the end of the pattern

        # Compare characters from the end of the pattern to its beginning
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1  # Move towards the beginning of the pattern

        # If the entire pattern matches, return its position in the text
        if j < 0:
            return i  # Substring found

        # Shift the index i based on the shift table
        # This allows "jumping" over non-matching parts of the text
        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

    # If the substring is not found, return -1
    return -1
