def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowel_map = {}
    phrase = phrase.lower()
    vowel = ["a", "e", "i", "o", "u"]
    for char in vowel:
        count = phrase.count(char)
        if not count ==0:
            vowel_map[char] = count
    return vowel_map
