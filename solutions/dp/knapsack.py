"""
Knapsack problem similar to a Rod Cutting problem is a common example of Dynamic
 Programming.

Imagine you have a list of items, each has an associated value and weight. You
 are also given a bag of a limited capacity (maximum weight it can hold). Your
 task is to maximise the value of items a bag can hold.

Example:
```
    Item Value Weight
      a    60    5          Bag capacity = 5.
      b    50    3
      c    70    4          Answer: 80 (item b and d).
      d    30    2
```
"""


def backtrack(I, c, i=None):
    """
    Top-down naive recursive solution to a Knapsack problem.

    This is an exhaustive recursive solution, similar to a rod cutting problem,
     that works for floating point weights and values.

    Complexity: O(2^n) where `n` is the total number of listed items
    :param list[Item] I: List of items
    :param int c: Maximum capacity a knapsack can hold
    :param int i: Index of current item (used in recursion)
    :return int: Maximum value gain
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
    """
    Knapsack solution for non-negative integer weights using DP.

    Uses similar logic as the recursive solution but uses DP table to store the
     state.

    :param list[Item] I: List of items
    :param int c: Maximum capacity a knapsack can hold
    :return int: Maximum value gain
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
    def __init__(self, v, w):
        """
        Knapsack item object representation.

        Using integer value and weight for simplicity

        :param int v: Item value
        :param int w: Item weight
        """
        self.value = v
        self.weight = w
