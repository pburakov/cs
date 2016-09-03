def base(I, b):
    """
    Base converter.

    Converts decimal number into base representation of 2 through 16.

    Complexity: O(n) pseudo-polynomial time where `n` is number of times integer can be
     divided by 2.
    :param int I: Decimal integer
    :param int b: Radix base
    :return str: Binary string
    """
    if not 1 < b <= 16:
        raise ValueError("Unable to convert to base {}".format(b))
    if I > 0:
        rem = I % b
        return base(I // b, b) + CHARS[rem]
    else:
        return ''


def gcd(a, b):
    """
    Returns greatest common divisor using Euclid's method.

    Complexity: O(n) where `n` is the larger number
    :param int a: First integer
    :param int b: Second integer
    :return int: GCD of two integers
    """
    while b:
        a, b = b, a % b
    return a


"""
Constants used in this module
"""
CHARS = "0123456789abcdef"
