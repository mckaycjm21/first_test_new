def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    factors = []
    new_list = list(range(1, num + 1))
    for nums in new_list:
        if num / nums % 1 == 0:
            print(nums)
            factors.append(nums)
    return factors