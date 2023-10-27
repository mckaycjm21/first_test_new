def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    new_set = set()
    count = 0
    highest_count = 0
    for num in nums:
        new_set.add(num)
    for ele in new_set:
        if nums.count(ele) > count:
            highest_count = ele
            count = nums.count(ele)
    return highest_count