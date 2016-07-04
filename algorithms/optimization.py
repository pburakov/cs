"""
Optimization problems can have many possible solutions, each of which has a
 value, and we wish to find one with the optimal (minimum or maximum) value.

Optimization problems are typically solved with the use of dynamic programming
 or DP. Although, there's no strong definition of the DP concept. DP usually
 involves some sort of memoization technique for recursive divide-and-conquer
 algorithms that repeatedly solve the same sub-problem, thus avoiding excessive
 computation.

When developing DP algorithm we follows these steps:
 1. Characterize the structure of _an_ optimal solution.
 2. Recursively define the value of an optimal solution.
 3. Compute the value of an optimal solution, typically in a bottom-up fashion.
 4. Construct _the_ optimal solution from computed information.

Below is a simple canonical template that may apply to many DP solutions.
"""


def memoize(f):
    """
    Memoization function decorator.

    Loads value from cache if it was already computed. Arguments of a function
     are required to be hashable to be stored in cache.

    Complexity: O(1) for storage and retrieval.
    :param (tuple)->(Any) f: Function
    :return Any: Return value of a function `f`
    """
    cache = {}

    def run(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]

    return run


@memoize
def fib(n):
    """
    Calculates n-th Fibonacci number recursively.

    Although Fibonacci formula is recursive in nature, simple recursion, as in
     many recurrent calculation problems, is not the optimal solution for it. This
     is a textbook Fibonacci example, optimized by memoization using a Python
     decorator function.

    Complexity: O(2^n) without optimization as each call invokes two more recursive
     calls. Time is reduced to linear O(n) with the use of memoization, which takes
     additional O(n) space.
    :param int n: Number in Fibonacci sequence
    :return int: `n`-th Fibonacci number
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
    """
    Calculates n-th Fibonacci number using DP.

    This is a canonical DP example. Although it is based on a recursive solution,
     it uses different memoization approach by keeping calculated values in an
     array.

    This template is used in many DP solutions. Some DP algorithms make use of
     multidimensional arrays to store solved states. To better understand this
     solution, try to represent its operations as a topologically sorted graph.

    Complexity: O(n) with O(n) additional storage space.
    :param int n: Number in Fibonacci sequence
    :return int: `n`-th Fibonacci number
    """
    DP = [0] * (n + 1)  # Allocating table to hold calculated values
    DP[1] = 1
    DP[2] = 1
    for i in range(3, n + 1):
        DP[i] = DP[i - 2] + DP[i - 1]
    return DP[n]
