"""
Knapsack Problem
================

Imagine you have a set of :math:`n` items :math:`i=1...n`, each has an associated value
:math:`V_i` and weight :math:`W_i`. You are also given a bag of a limited maximum weight
it can hold :math:`c`. Your task is to maximize the value of items a bag can hold.

Example::

    #  i  Value Weight
    #  0    60    5
    #  1    50    3
    #  2    70    4
    #  3    30    2

    (W=[5, 3, 4, 2], V=[60, 50, 70, 30], c=5) -> 80  # (items with index 1 and 3)

The decision problem form of the knapsack problem is NP-complete, thus there is no known
algorithm both correct and fast (polynomial-time) in all cases. There is a
pseudo-polynomial time algorithm using dynamic programming, discussed below.

Knapsack problem is a classic example of Dynamic Programming, similar to a Rod-Cutting
problem. It is described in detail in the book "Elements of Programming Interviews" by A.
Aziz et al.
"""


def max_value(W, V, c, i=0):
    """Returns maximum value for a given list or items and knapsack capacity.

    This is an exhaustive recursive solution, similar to a rod cutting problem. The
    algorithm is named "0/1" because at each step, we make a decision, whether we take
    an item or not.

    Complexity:
        :math:`O(2^n)`.

    :param list W: Item weights.
    :param list V: Item values.
    :param int c: Maximum capacity a knapsack can hold.
    :param int i: Index of current item (used in recursion).
    :return: Maximum value gain.

    """
    if i >= min(len(W), len(V)):
        return 0
    if W[i] > c:  # Item is heavier than the knapsack capacity
        return max_value(W, V, c, i + 1)
    else:
        # Definition of 0/1 recursive formula:
        return max(
            V[i] + max_value(W, V, c - W[i], i + 1),  # With item
            max_value(W, V, c, i + 1)  # Without item
        )


def max_value_dp(W, V, c):
    """0/1 Knapsack problem solution for non-negative integer weights using DP.

    The algorithm is the same as the recursive solution but uses DP table to maintain
    the state.

    Complexity:
        :math:`O(nc)`.

    :param list W: Item weights.
    :param list V: Item values.
    :param int c: Maximum capacity a knapsack can hold.
    :return: Maximum value gain.

    """
    n = min(len(W), len(V))
    cache = [[0 for _ in range(0, c + 1)] for _ in range(0, n + 1)]
    for i in range(0, n + 1):
        for c in range(0, c + 1):
            if i == 0 and c == 0:
                cache[i][c] = 0
            elif W[i - 1] > c:
                cache[i][c] = cache[i - 1][c]
            else:
                cache[i][c] = max(
                    V[i - 1] + cache[i - 1][c - W[i - 1]],
                    cache[i - 1][c]
                )
    return cache[n][c]
