"""
Base Conversion
===============

In mathematics, a base or *radix* is the number of different digits or combination of
digits and letters that a system of counting uses to represent numbers. The most common
base used today is the decimal system, which uses the 10 digits from 0 to 9. In
computing, base 2 is used because at the most simple level, computers can only deal with
``0`` and ``1`` bit. Hexadecimal (base 16) is used because of how computers group binary
digits together. Every four binary digits turn into one hexadecimal digit when changing
between them. Because there are more than 10 digits in hexadecimal, the six digits after
9 are shown as A, B, C, D, E, and F.
"""


def base(I, b, charset="0123456789abcdef"):
    """Base converter.

    Converts decimal number into a base representation supported by a given charset.

    Complexity:
        :math:`O(n)` pseudo-polynomial time where :math:`n` is number of times integer can
        be divided by radix base.

    :param int I: Decimal integer.
    :param int b: Radix base.
    :param str charset: Ordered charset (default is a hexadecimal charset).
    :return: Base representation as a string.

    """
    if not 1 < b <= len(charset):
        raise ValueError("Unable to convert to base {}".format(b))
    if I > 0:
        rem = I % b
        return base(I // b, b) + charset[rem]
    else:
        return ''
