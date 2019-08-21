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


def is_prime(n):
    """Evaluates if a number is a prime using 6k±1 method.

    A trivial way to test for primality is called trial division method. Given an input
    number :math:`n`, check whether any prime integer :math:`m\\in 2...\sqrt n` evenly
    divides :math:`n` (the division leaves no remainder). If :math:`n` is divisible by any
    :math:`m` then :math:`n` is composite, otherwise it is prime.

    :math:`6k±1` algorithm is an improvement over trial division. We observe that all
    primes greater than :math:`6` are of the form :math:`6k±1`. This is because all
    integers can be expressed as :math:`(6k+i)` for some integer :math:`k` and for
    :math:`i=−1,0,1,2,3`, or :math:`4`; :math:`2` divides :math:`(6k+0),(6k+2),(6k+4)`; and
    :math:`3` divides :math:`(6k+3)`. So, a more efficient method is to test if :math:`n`
    is divisible by :math:`2` or :math:`3`, then to check through all the numbers of the
    form :math:`6k±1≤\sqrt n`. This is 3 times as fast as testing all :math:`m`.

    Complexity:
        :math:`O(\sqrt n)`.

    :param int n: Input integer.
    :return: :data:`True` is number is a prime, :data:`False` otherwise.

    """
    if n <= 3:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


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
