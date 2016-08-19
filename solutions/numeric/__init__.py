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
