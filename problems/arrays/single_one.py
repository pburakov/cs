"""
Single One
==========

Given an array of integers, every element appears twice except for one. Find that single
one.

Example::

    [1, 2, 2, 3, 1] -> 3

"""


def single_one(A):
    """Finds a single element in an array.

    The algorithm scans the array and constructs a frequency map.

    Complexity:
        :math:`O(n)` time, :math:`O(n)` space for frequency map.

    :param list A: Input array.
    :return: A single element.

    """
    M = {}
    for i in A:
        if i not in M:
            M[i] = 0
        M[i] += 1
    for i in M:  # Find a single one in a frequency map
        if M[i] < 2:
            return i
    return 0


def single_one_adv(A):
    """Finds a single element in an array.

    The algorithm uses binary XOR operation to find the element.

    Complexity:
        :math:`O(n)` time, no extra space.

    :param list A: Input array.
    :return: A single element.

    """
    out = 0
    n = len(A)
    for i in range(0, n):
        out ^= A[i]
    return out
