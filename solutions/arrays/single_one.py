"""
Given an array of integers, every element appears twice except for one. Find that single
 one.

Input : [1, 2, 2, 3, 1]
Output : 3
"""


def freq_map(A):
    """
    Linear solution using frequency map.

    Straightforward algorithm that scans the array and constructs a frequency map.

    Complexity: O(n) time, O(n) space for frequency map
    :param list[int] A: Input array
    :return int: Missing number
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


def binary(A):
    """
    Linear solution using binary logic.

    Complexity: O(n) time, no extra space (except the output)
    :param list[int] A: Input array
    :return int: Missing number
    """
    out = 0
    n = len(A)
    for i in range(0, n):
        out ^= A[i]
    return out
