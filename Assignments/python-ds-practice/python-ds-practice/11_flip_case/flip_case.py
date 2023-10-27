def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    to_swap_upper = to_swap.upper()
    to_swap_lower = to_swap.lower()
    new_string = ""
    for char in phrase:
        if char == to_swap_upper:
            new_string = new_string + char.lower()
        elif char == to_swap_lower:
            new_string = new_string + char.upper()
        else:
            new_string = new_string + char
    return new_string