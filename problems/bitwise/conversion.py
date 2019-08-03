"""
Conversion
==========

Write a program to determine the number of bits you need to flip to convert integer :math:`a`
to integer :math:`b`.

Example::

    29 (11101), 15 (01111) -> 2
"""


def conversion(a, b):
    """Computes the number of bits to flip to convert a to b.

    The algorithm uses XOR function to determine the difference.

    :param int a: Input integer.
    :param int b: Input integer.
    :return: The number of bits to flip.

    """
    count = 0
    d = a ^ b  # flip only bits that differ
    while d:
        count += d & 1
        d = d >> 1
    return count
