def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    letter_count_dict = {}
    phrase_set = [phrase]
    for char in phrase:
        print(char)
        letter_count_dict[char] = phrase.count(char)
    return letter_count_dict
