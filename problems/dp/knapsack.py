"""
Knapsack Problem
================

Imagine you have a list of items, each has an associated value and weight. You are also
given a bag of a limited capacity (maximum weight it can hold). Your task is to maximise
the value of items a bag can hold.

Example::

    Item Value Weight
      a    60    5          Bag capacity = 5.
      b    50    3
      c    70    4          Answer: 80 (items b and d).
      d    30    2

Knapsack problem is a classic example of Dynamic Programming, similar to a Rod-Cutting
problem. It is described in detail in the book "Elements of Programming Interviews" by A.
Aziz et al.
"""


def backtrack(I, c, i=None):
    """Top-down naive recursive solution to a 0/1 Knapsack problem.

    This is an exhaustive recursive solution, similar to a rod cutting problem, that works
    for floating point weights and values. The principle is the same as partitions
    generation algorithm. At each step we decide whether we want to take an item or not,
    hence the name "0/1".

    Complexity:
        :math:`O(2^n)` where :math:`n` is the total number of listed items.

    :param list[Item] I: List of items.
    :param int c: Maximum capacity a knapsack can hold.
    :param int i: Index of current item (used in recursion).
    :return: Maximum value gain.

    """
    if i is None:  # Initializing `i`
        i = len(I)
    if i == 0 or c == 0:
        return 0
    if I[i - 1].weight > c:  # Item is larger than the knapsack capacity
        return backtrack(I, c, i - 1)
    else:
        w = I[i - 1].weight
        v = I[i - 1].value
        return max(
            v + backtrack(I, c - w, i - 1),  # With item
            backtrack(I, c, i - 1)  # Without item
        )


def dp(I, c):
    """0/1 Knapsack problem solution for non-negative integer weights using DP.

    Uses similar logic as the recursive solution but uses DP table to store the state.

    Complexity:
        :math:`O(nc)`, can be reduced to :math:`O(c)` time and space if values are
        re-written in a 1-dimensional array on every iteration.

    :param list[Item] I: List of items.
    :param int c: Maximum capacity a knapsack can hold.
    :return: Maximum value gain.

    """
    n = len(I)
    DP = [[0 for _ in range(0, c + 1)] for _ in range(0, n + 1)]
    for i in range(0, n + 1):
        for c in range(0, c + 1):
            if i == 0 and c == 0:
                DP[i][c] = 0
            elif I[i - 1].weight > c:
                DP[i][c] = DP[i - 1][c]
            else:
                w = I[i - 1].weight
                v = I[i - 1].value
                DP[i][c] = max(
                    v + DP[i - 1][c - w],
                    DP[i - 1][c]
                )
    return DP[n][c]


"""
Data structures used in the solution
"""


class Item:
    """Knapsack item object representation.

    :ivar v: Item value.
    :ivar w: Item weight.

    """
    def __init__(self, v, w):
        """Knapsack item object representation.

        Using integer value and weight for simplicity

        :param int v: Item value.
        :param int w: Item weight.
        """
        self.value = v
        self.weight = w
