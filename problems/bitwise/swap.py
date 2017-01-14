"""
Swap in-place

Swaps two integers without using extra memory.
"""


def swap(a, b):
    """Swaps two integers in a tuple without using extra memory.

    This algorithm is based on properties of XOR operation. Binary values are "flipped"
    twice against each other.

    Complexity:
        :math:`O(1)`, no extra space.

    :param int a: Input integer
    :param int b: Input integer
    :return: Tuple of two swapped integers

    """
    a ^= b
    b ^= a
    a ^= b
    return a, b
