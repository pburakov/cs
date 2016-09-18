def memoize(f):
    """
    Memoization function decorator.

    Loads value from cache if it was already computed. Arguments of a function need to
     be hashable to be stored in cache. This is Python-specific implementation,
     applicable to simple cases of recursive functions.

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

    Although Fibonacci formula is recursive in nature, simple recursion, as in many
     recurrent calculation problems, is not an optimal solution for it. This is a
     textbook Fibonacci example, optimized with memoization by Python decorator.

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

    This is a canonical DP example. Although it is based on a recursive solution, it
     uses different memoization technique by keeping calculated values in an array. Most
     DP algorithms make use of arrays to store solved states, including multidimensional
     arrays.

    This template is used in many DP solutions. To better understand it, try to
     represent its operation as a topologically sorted graph and think about the
     relations between vertices. In this case there's only one way to get to the `i`-th
     vertex, which is to calculate vertices `i-2` and `i-1`. There's also the same cost
     of getting there, consider it to be a weight of `1`. In many DP problems there is
     more than one way to reach a vertex with different costs associated with each.

    Lastly, in many DP problems saved calculations usually are not so obvious as in this
     example. Often they need to be interpreted or "traced back" in order to return a
     final solution for a given problem.

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
