"""
Add one
=======

Write a program to add one to a given number. The use of arithmetic operators ``+``, ``-``,
``*``, ``/`` is not allowed.

Problem is discussed in more detail here:
https://www.geeksforgeeks.org/add-1-to-a-given-number/
"""


def solution(x):
    """Adds one to the input integer without using arithmetic logic.

    The solution is using binary logic for addition. To add :math:`1` to a number :math:`x`
    (for example ``0011000111``), flip all the bits after the rightmost 0 bit (the result is
    ``0011000000``). Finally, flip the rightmost :math:`0` bit also (the result is
    ``0011001000``) to get the answer.

    Complexity:
        :math:`O(\log n)`, where :math:`n` is the input number.

    :param int x: Input number.
    :return: Output number.
    """
    m = 1
    # Flip all set bits one by one until we find 0
    while x & m:
        x ^= m
        m <<= 1
    x ^= m
    return x
