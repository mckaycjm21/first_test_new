def print_upper_words(list_words, check_for):
    """This function will take your list of words and return them
    uppercased and seperated by each word"""
    # This is a loop iterating through the list pulling the words
    # out individually based on a "check_for" parameter input from
    # the user.
    for word in list_words:
        if(word[0] == check_for):
            print(word.upper())
        else:
            print(f"{word} does not begin with a {check_for}")
            


print_upper_words(["hello", "hey", "goodbye", "yo", "yes", "earnest"], "h")