def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1 = str(num1)
    num2 = str(num2)
    num1_list = []
    num2_list = []
    for num in num1:
        num = int(num)
        num1_list.append(num)
    for num in num2:
        num = int(num)
        num2_list.append(num)
    num1_list = sorted(num1_list)
    num2_list = sorted(num2_list)
    if num1_list == num2_list:
        return True
    else:
        return False