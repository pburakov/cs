"""
Rod-Cutting Problem
===================

Imagine we have a rod and we can cut it to pieces of integral lengths. Each length has a
price, and our task is to cut to get the maximum profit for any given length if possible.
Given length may not exceed the maximum length we have in our "price-list".

For example, given the price chart :math:`P=[0, 1, 5, 8, 9]`, where :math:`P[i]` is the
profit for cut of length :math:`i`, and a total length of :math:`n=4`, the optimal strategy
would be to make two cuts of length :math:`2` which will result in maximum gain of
:math:`10` and not :math:`9`, if we simply picked the largest one.

This problem is described in detail in CLRS book (Introduction to Algorithms).

"""


def backtrack(P, n):
    """Rod cutting problem solver using a recursive algorithm.

    This is a highly inefficient top-down recursive algorithm which checks every possible
    option numerous times unless memoization technique is used. The principle is the same
    as partitions generation algorithm (we decide whether we want to cut the rod at this
    point of not), although it doesn't use as much space, since we only care about the
    maximum revenue.

    Complexity:
        :math:`O(2^n)` time and space, because for every :math:`i` we decide whether to
        make the cut or not.

    :param list[float] P: Prices for cuts :math:`\{0..k\}`.
    :param int n: Total length :math:`n≤k`.
    :return: Maximum price.

    """
    if n < 1:
        return 0.0
    else:
        q = -inf
        for i in range(1, n + 1):
            # Is revenue bigger if we cut at `i` or if we don't?
            q = max(q, P[i] + backtrack(P, n - i))  # Note the `n-i` here
        return q


def memoized(P, n, cache=None):
    """Memoized rod cutting problem solver.

    Now that we know the recursive formula, we observe that computations are repeated
    several times for same :math:`n`, we can apply simple memoization and ensure that
    every :math:`n` is computed exactly once.

    This is an excellent example of evolution of a dynamic programming solution from a
    recursion.

    Complexity:
        :math:`O(n)` with :math:`O(n)` use of memory stack for recursion.

    :param list[float] P: Prices for cuts :math:`\{0..k\}`.
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
                q = max(q, P[i] + memoized(P, n - i, cache))
                cache[n] = q
        return cache[n]


def dp(P, n):
    """Rod cutting problem solver using bottom-up DP.

    We can optimize the solution even further without use of recursion. Solution uses
    almost the same formula, as the DP solution for Fibonacci numbers.

    Complexity:
        :math:`O(n)` time, :math:`O(n)` space for DP array.

    :param list[float] P: Prices for cuts :math:`\{0..k\}`.
    :param int n: Total length :math:`n≤k`.
    :return: Maximum price.

    """
    k = len(P)
    DP = [float] * k
    DP[0] = 0.0
    for i in range(1, n + 1):
        q = -inf
        for j in range(1, i + 1):
            q = max(q, P[j] + DP[i - j])
        DP[i] = q
    return DP[n]


"""
Constants used in the solution
"""
inf = float("inf")
