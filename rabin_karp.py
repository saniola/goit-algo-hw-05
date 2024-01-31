def polynomial_hash(s, base=256, modulus=101):
    """
    Returns the polynomial hash of the string s.
    """
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value


def rabin_karp(main_string, substring):
    # Lengths of the main string and the search substring
    substring_length = len(substring)
    main_string_length = len(main_string)

    # Base number for hashing and modulus
    base = 256
    modulus = 101

    # Hash value for the search substring and the current slice in the main string
    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)

    # Previous value for hash recalculation
    h_multiplier = pow(base, substring_length - 1) % modulus

    # Iterate through the main string
    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i : i + substring_length] == substring:
                return i

        if i < main_string_length - substring_length:
            current_slice_hash = (
                current_slice_hash - ord(main_string[i]) * h_multiplier
            ) % modulus
            current_slice_hash = (
                current_slice_hash * base + ord(main_string[i + substring_length])
            ) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus

    return -1
