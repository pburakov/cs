"""
Memoization is considered to be a part of a dynamic approach to solving a problem.
 Universal memoize function decorator is implemented below.

For examples of use of memoization see fibonacci.py in /exercises folder.
"""


def memoize(f):
    """
    Pythonic memoization decorator.

    Will return value from `cache` for function `f` if it was already
     calculated for given list of arguments `*args`.
    """
    cache = {}

    def helper(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]

    return helper
