inf = float("inf")


def cut_rod(P, n):
    """
    Rod cutting problem solver using recursive algorithm.

    This is an excellent example of dynamic programming approach, discussed in detail
     in CLRS book (Introduction to Algorithms).

    Imagine we have a rod and we can cut it to pieces of integral lengths. Each
     length has a price, and our task is to cut to get the maximum profit for any
     given length if possible. Given length may not exceed the maximum length we have
     in our "price-list".

    Example:
     Given the price chart `P=[0, 1, 5, 8, 9]`, where `P[i]` is the profit for cut of
     length `i`, and a total length of `n=4`, the optimal strategy would be to make
     two cuts of length `2` which will result in maximum gain of `10` and not `9`.

    This is a highly inefficient top-down recursive algorithm which checks every
     possible option numerous times unless memoization technique is used. The principle
     is the same as partitions generation algorithm (we decide whether we want to cut
     the rod at this point of not), although it doesn't use as much space, since we
     only care about the maximum revenue.

    Complexity: O(2^n) time and space, because for every `i` we decide whether to make
     the cut or not.
    :param list[float] P: Prices for cuts {0..k}
    :param int n: Total length `n≤k`
    :return float: Maximum price
    """
    if n < 1:
        return 0.0
    else:
        q = -inf
        for i in range(1, n + 1):
            # Is revenue bigger when we cut at `i` and when we don't
            q = max(q, P[i] + cut_rod(P, n - i))  # Note the `n-i` here
        return q


def cut_rod_memo(P, n, cache=None):
    """
    Memoized rod cutting problem solver.

    Now that we know the recursive formula for the solution and we observe that
     computations are repeated several times for same `n`, we can apply simple
     memoization and ensure that every `n` is computed exactly once.

    Complexity: O(n) with O(n) use of memory stack for recursion
    :param list[float] P: Prices for cuts {0..k}
    :param int n: Total length `n≤k`
    :param dict cache: Hash table of memoized values
    :return float: Maximum price
    """
    if cache is None:
        cache = {}  # Initialize the cache
    if n < 1:
        return 0.0
    else:
        if n not in cache:
            q = -inf
            for i in range(1, n + 1):
                q = max(q, P[i] + cut_rod_memo(P, n - i, cache))
                cache[n] = q
        return cache[n]


def cut_rod_dp(P, n):
    """
    Rod cutting problem solver using bottom-up DP

    We can optimize the solution even further without use of recursion. Solution is
     similar to Fibonacci example.

    Complexity: O(n) time, O(n) space for DP array
    :param list[float] P: Prices for cuts {0..k}
    :param int n: Total length `n≤k`
    :return float: Maximum price
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


p1 = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

print(cut_rod(p1, 10))
print(cut_rod_memo(p1, 10))
print(cut_rod_dp(p1, 10))
