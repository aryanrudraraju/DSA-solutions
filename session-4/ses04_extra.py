def check_sorted(L):
    """
    Uses looping to check whether a list is sorted or not (could be increasing or decreasing).
    Examples:
    >>> check_sorted([3, 6, 48, 24, 51, 262, 119])
    False
    >>> check_sorted([748, 623, 424, 414, 74, 2])
    True
    >>> check_sorted([1, 2, 3])
    True
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW THIS
    is_increasing = True
    is_decreasing = True

    for i in range(len(L) - 1):
        if L[i] > L[i+1]:
            is_increasing = False
        if L[i] < L[i+1]:
            is_decreasing = False

    return is_increasing or is_decreasing



def longest_sorted(L):
    """
    Uses looping to return the longest sorted sequence in a list (ascending).
    Examples:
    >>> longest_sorted([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 13, 15, 3, 11, 7, 5])
    [1, 9, 13, 15]
    >>> longest_sorted([25, 72, 31, 32, 8, 20, 38, 43, 85, 39, 33, 40, 98, 37, 14])
    [8, 20, 38, 43, 85]
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW THIS
    longest = []
    current = []

    for i in range(len(L)):
        if i == 0 or L[i] > L[i-1]:
            current.append(L[i])
        else:
            if len(current) > len(longest):
                longest = current
            current = [L[i]]

    if len(current) > len(longest):
        longest = current

    return longest