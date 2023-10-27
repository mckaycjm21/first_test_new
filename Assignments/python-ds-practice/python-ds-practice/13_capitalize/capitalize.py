def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    first_letter = phrase[0].upper()
    phrase = (phrase[1:])
    print(phrase)
    phrase = ''.join((first_letter, phrase))
    return phrase