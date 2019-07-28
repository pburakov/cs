"""
Primes and Primality Testing
============================

This module demonstrates some useful algorithms used in cryptography.
"""


def gcd(a, b):
    """Calculates greatest common divisor using Euclid's method.

    Complexity:
        :math:`O(k)` where :math:`k` is the number of digits in a larger number.

    :param int a: First integer.
    :param int b: Second integer.
    :return: GCD of the two integers.
    """
    while b:
        a, b = b, a % b
    return a


def totient(n):
    """Euler's totient function.

    Euler's totient function (also called Euler's :math:`\phi` (phi) function) counts the
    positive integers up to a given integer :math:`n` that are relatively prime to
    :math:`n`. :math:`\phi(n)` is the number of integers :math:`k` in range
    :math:`1 ≤ k ≤ n` for which the greatest common divisor :math:`gcd(k,n)=1`.

    For example, the totatives of :math:`n=9` are :math:`\{1, 2, 4, 5, 7, 8\}`. All numbers
    in this set are relatively prime to 9, therefore :math:`\phi (9) = 6`.

    :math:`\phi` plays a key role in the definition of RSA encryption system. This is a
    naive implementation of :math:`\phi` function. More optimal algorithms can be derived
    from Euler's product formula which states that the value of totient function is a
    product over all prime factors :math:`p` of :math:`n`:
    :math:`\phi(n)=n\\prod_{p|n}(1-\\frac{1}{p})`.

    Complexity:
        :math:`O(n\log k)`. There can be at most :math:`k=\log_{10} n` digits in all positive
        numbers up to :math:`n`.

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

    Complexity:
        :math:`O(1)`.

    :param int n: Input integer.
    :return: :data:`True` is number is a probable prime, :data:`False` otherwise.

    """
    if n == 2:
        return True
    if not n & 1:
        return False
    return pow(2, n - 1, n) == 1


def primes():
    """An infinite generator of sequence of prime numbers.

    This generator implements dynamically populated Sieve of Eratosthenes.

    Composite numbers and all their found divisors are stored in a hash table as the
    generator runs forward.

    :return: Next prime.

    """
    D = {}
    q = 2  # integer tested for primality
    while True:
        if q not in D:
            yield q  # new prime is found
            D[q * q] = [q]  # add q's next multiple - it's not prime by definition
        else:
            # q is not prime. p = D[q] is the list of primes that were found dividing it.
            # Add next multiple of p - it's also not prime by definition
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]  # discard since values < q are no longer needed
        q += 1
