"""
A DP is an algorithmic technique which is usually based on a recurrent formula
 and one (or some) starting states. A sub-solution of the problem is constructed
 from previously found ones. DP solutions have a polynomial complexity which
 assures a much faster running time than other techniques like backtracking,
 brute-force etc.

For examples, see dp.py in /exercies folder.

Dynamic approach is often similar to recursive solution that includes caching
 or memoization strategy. Universal memoize function decorator is implemented below.

For exmples of use of memoization see fibonacci.py in /exercises folder.
"""


def memoize(f):
    """
    Pythonic memoization decorator.

    Will return value from `memo` dict cache for function `f` if it was already
     calculated for given list of arguments `*args`.
    """
    memo = {}

    def helper(*args):
        if args not in memo:
            memo[args] = f(*args)
        return memo[args]

    return helper
