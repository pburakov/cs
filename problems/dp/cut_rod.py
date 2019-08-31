"""
Rod-Cutting Problem
===================

Imagine we have a rod and we can cut it to pieces of integral lengths. Each length has a
price, and our task is to cut to get the maximum profit for any given length if possible.
A given length may not exceed the maximum length we have in our "price-list".

For example, given the price chart :math:`P=[0, 1, 5, 8, 9]`, where :math:`P[i]` is the
profit for cut of length :math:`i`, and a total length of :math:`n=4`, the optimal strategy
would be to make two cuts of length :math:`2` which will result in maximum gain of
:math:`10` and not :math:`9`, if we simply picked the largest one.

Example::

    (P=[0, 1, 5, 8, 9], n=4) -> 10

This problem is described in detail in CLRS book (Introduction to Algorithms).

"""


def max_price(P, n):
    """Calculates the maximum price for a given rod length, based on a price-list.

    This is a highly inefficient top-down recursive algorithm which checks every possible
    option numerous times, unless the memoization technique is used. The principle is the
    same as the partition generation algorithm. At each step, we decide whether we want to
    cut the rod or not, and we calculate the maximum revenue for each outcome.

    Complexity:
        :math:`O(2^n)`.

    :param list P: Prices for cuts :math:`\{0..k\}`.
    :param int n: Total length :math:`n≤k`.
    :return: Maximum price.

    """
    if n < 1:
        return 0.0
    else:
        q = -inf
        for i in range(1, n + 1):
            # Is the revenue bigger if we cut at `i` or if we don't?
            q = max(q, P[i] + max_price(P, n - i))  # Note the `n-i` here
        return q


def max_price_dp(P, n, cache=None):
    """Calculates the maximum price for given rod length, based on the price-list.

    Now that we know the recursive formula, we observe that computations are repeated
    several times for the same :math:`n`. We can use a simple memoization technique to
    ensure that every :math:`n` is computed exactly once.

    This is an excellent example of evolution of a dynamic programming solution from a
    recursion.

    Complexity:
        :math:`O(n)` due to the use of memoization.

    :param list P: Prices for cuts :math:`\{0..k\}`.
    :param int n: Total length :math:`n≤k`.
    :param dict cache: Hash table of memoized values.
    :return Maximum price.

    """
    if cache is None:
        cache = {}  # Initialize the cache
    if n < 1:
        return 0.0
    else:
        if n not in cache:
            q = -inf
            for i in range(1, n + 1):
                q = max(q, P[i] + max_price_dp(P, n - i, cache))
                cache[n] = q
        return cache[n]


def max_price_adv(P, n):
    """Calculates the maximum price for given rod length, based on the price-list.

    We can optimize the solution even further without the use of recursion.

    Complexity:
        :math:`O(n)` time, :math:`O(n)` space for a DP cache.

    :param list[float] P: Prices for cuts :math:`\{0..k\}`.
    :param int n: Total length :math:`n≤k`.
    :return: Maximum price.

    """
    cache = [0.0]
    for i in range(1, n + 1):
        q = -inf
        for j in range(1, i + 1):
            q = max(q, P[j] + cache[i - j])
        cache[i] = q
    return cache[n]


"""
Constants used in the solution
"""
inf = float("inf")
