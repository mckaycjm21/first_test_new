def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    new_phrase = ""
    phrase = phrase.split(" ", 2)
    for word in phrase:
        first_letter = word[0].upper()
        word = word[1:].lower()
        new_phrase = f"{new_phrase} {first_letter}{word}"
    return new_phrase[1:]
