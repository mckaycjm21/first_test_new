def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    open_parens_count = parens.count("(")
    close_parens_count = parens.count(")")
    if open_parens_count == close_parens_count:
        if "(" == parens[len(parens) - 1]:
            return False
        if ")" == parens[0]:
            return False
        return True
    else:
        return False