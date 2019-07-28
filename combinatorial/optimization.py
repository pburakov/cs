"""
Dynamic Programming
===================

**Dynamic programming** is a technique used to explore the combinatorial search space more
efficiently. The two key attributes a problem must have in order for DP to be applicable
are the overlapping sub-problems and optimal substructure. DP solution usually involves
some sort of **memoization** technique. Solutions are built on sub-problems that already
have been solved to optimality, or are being solved repeatedly.

DP solution is rearely obvious. A suggested first step is to find a recursive solution.
The second step is finding a state or a configuration that can be saved and reused.
A helpful technique is describing state transitions as a graph problem to which a shortest
or longest path algorithm can be applied. In fact, Richard Bellman, one of the contributors
to Bellman-Ford algorithm, was the one who developed the idea of dynamic programming.

To better understand DP, try to represent path to optimality as a topologically sorted
graph and think about the relations between vertices. In many cases the only way to get to
the :math:`i`-th solution is to calculate vertices :math:`i-2` and :math:`i-1`. In many DP
problems, there is more than one way to reach the optimum with different costs associated.
Sometimes the graph of "cached" solutions needs to be traversed again in order to locate an
optimal solution.

Some famous DP problems include: Knapsack, Rod Cutting, Edit Distance, Longest Common
Subsequence, Longest Increasing Sequence, Coin Change, Matrix Multiplication, Text
Justification, Max Cost Grid Path and many more.

Below are some basic DP templates, that help introducing the concept. However, practical
applications of DP go well beyond these examples and require substantial amount of practice.
"""
from functools import wraps


def memoize(f):
    """Memoization function decorator.

    Loads value from cache if a solution for given function arguments was already computed.

    Complexity:
        `O(1)` for storage and retrieval.

    :param (tuple)->(Any) f: Function.
    :return: Return value of a function.

    """
    cache = {}

    @wraps(f)
    def run(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]

    return run


@memoize
def fib(n):
    """Calculates n-th Fibonacci number recursively.

    The formula for :math:`n`-th Fibonacci number is :math:`F_n=F_{n-2}+F_{n-1}`.

    Although Fibonacci formula is recursive in nature, recursion, as in many recurrent
    computation problems, is not an optimal solution for it.

    This is a textbook Fibonacci example, optimized with memoization by Python decorator.

    Complexity:
        :math:`O(2^n)` without optimization as each call invokes two more recursive calls.
        Time is reduced to linear :math:`O(n)` with the use of memoization decorator.
        Memoization takes additional :math:`O(n)` space.

    :param int n: Number in Fibonacci sequence.
    :return: :math:`n`-th Fibonacci number.

    """
    if n < 0:
        raise ValueError("Invalid input")
    if n == 0:
        return 0
    if n <= 2:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)


def fib_dp(n):
    """Calculates n-th Fibonacci number using DP.

    This is a canonical DP example. Calculated values are kept in a cache. Most DP
    algorithms make use of one- or multi-dimensional arrays, or hash tables to store
    computations.

    Complexity:
        :math:`O(n)` with :math:`O(n)` additional storage space.

    :param int n: Number in Fibonacci sequence.
    :return: :math:`n`-th Fibonacci number.

    """
    DP = [0] * (n + 1)  # Allocating table to hold calculated values
    DP[1] = 1
    DP[2] = 1
    for i in range(3, n + 1):
        DP[i] = DP[i - 2] + DP[i - 1]
    return DP[n]


@memoize
def pascal(n, k):
    """Calculates the k-th term in n-th line of Pascal's triangle.

    Pascal's triangle is a triangular array of the binomial coefficients. The term in the
    :math:`n`-th row and :math:`k`-th column of Pascal's triangle is denoted as:
    :math:`{n\\choose k}={n-1\\choose k-1}+{n-1\\choose k}`. For example, row 4, column 2
    in Pascal's triangle is calculated as: :math:`{4\\choose2}=\\frac{4!}{2!(4-2)!}=6`.

    First 6 lines of Pascal's triangle can be written as::

                  1
                1   1
              1   2   1
            1   3   3   1
          1   4   6   4   1
        1   5  10   10  5   1

    Note that the terms in Pascal's triangle start with :math:`{0\\choose 0}=1`.

    Complexity:
        :math:`O(2^n)` without optimization as each call invokes two more recursive calls.
        Time is reduced to linear :math:`O(n)` with the use of memoization decorator.
        Memoization takes additional :math:`O(n)` space.

    :param n: Row number.
    :param k: Column number.
    :return: k-th term in the n-th row of Pascal's triangle.

    """
    if n == 0:
        return 1
    if k == 0 or k == n:
        return 1
    return pascal(n - 1, k - 1) + pascal(n - 1, k)


def pascal_dp(n):
    """Calculates terms in the n-th row of Pascal's triangle.

    The combinatorial formula for a term in Pascal's triangle for row :math:`n` and column
    :math:`k+1` can be written as :math:`C(n,k+1) = C(n,k) \\times \\frac{n-k}{k+1}`, where
    :math:`k \\in \{0,1,2...n\}`.

    For example :math:`C(4,2)=C(4,1)\\times \\frac{n-k}{k+1}=4 \\times \\frac{3}{2}=6`.

    Note that we can use dynamic list as a cache to memoize :math:`C(n,k)`. Conveniently,
    a complete cache represents an entire row.

    Complexity:
        :math:`O(n)` with :math:`O(n)` additional storage space.

    :param n: Row number.
    :return: List of terms in the n-th row of Pascal's triangle.

    """
    L = [1]
    for k in range(n):
        L.append(L[k] * (n - k) // (k + 1))
    return L
