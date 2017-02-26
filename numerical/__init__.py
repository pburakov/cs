"""
Numerical Algorithms
====================
"""


def base(I, b):
    """Base converter.

    Converts decimal number into base representation of :math:`2` through :math:`16`.

    Complexity:
        :math:`O(n)` pseudo-polynomial time where :math:`n` is number of times integer can
        be divided by radix base.

    :param int I: Decimal integer.
    :param int b: Radix base.
    :return: Base representation as a string.
    """
    if not 1 < b <= 16:
        raise ValueError("Unable to convert to base {}".format(b))
    if I > 0:
        rem = I % b
        return base(I // b, b) + CHARS[rem]
    else:
        return ''


def gcd(a, b):
    """Returns greatest common divisor using Euclid's method.

    Complexity:
        :math:`O(n)` where :math:`n` is the larger number.

    :param int a: First integer.
    :param int b: Second integer.
    :return: GCD of two integers.
    """
    while b:
        a, b = b, a % b
    return a


def totient(n):
    """Euler's totient function.

    Euler's totient function (also called Euler's :math:`\phi` (phi) function) counts the
    positive integers up to a given integer n that are relatively prime to n. It's the
    number of integers :math:`k` in range :math:`1 ≤ k ≤ n` for which the greatest common
    divisor :math:`gcd(k, n) = 1`.

    For example, the totatives of :math:`n=9` are :math:`\{1, 2, 4, 5, 7, 8\}`. All numbers
    in this set are relatively prime to 9, therefore :math:`\phi (9) = 6`.

    This function plays a key role in the definition of RSA encryption system.

    Complexity:
        :math:`O(n^2)`.

    :param int n: Input integer.
    :return: Number of relatively prime numbers in sequence.
    """
    count = 0
    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            count += 1
    return count


def is_probable_prime(n):
    """Evaluates if a number is a probable prime using Fermat method.

    :param int n: Input integer.
    :return: :data:`True` is number is a probable prime, :data:`False` otherwise.

    """
    if n == 2:
        return True
    if not n & 1:
        return False
    return pow(2, n - 1, n) == 1


"""
Constants used in this module
"""
CHARS = "0123456789abcdef"
