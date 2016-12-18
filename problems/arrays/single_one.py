"""
Single One
==========

Given an array of integers, every element appears twice except for one. Find that single
one.

Example::

    Input : [1, 2, 2, 3, 1]
    Output : 3

"""


def solution(A):
    """Linear solution using frequency map.

    Straightforward algorithm that scans the array and constructs a frequency map.

    Complexity:
        :math:`O(n)` time, :math:`O(n)` space for frequency map.

    :param list[int] A: Input array.
    :return: Missing integer.

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


def solution_advanced(A):
    """Linear solution using binary logic.

    Advanced solution using XOR operation.

    Complexity:
        :math:`O(n)` time, no extra space (except the output).

    :param list[int] A: Input array.
    :return: Missing integer number.

    """
    out = 0
    n = len(A)
    for i in range(0, n):
        out ^= A[i]
    return out
