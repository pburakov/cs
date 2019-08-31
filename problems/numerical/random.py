"""
Bound Randomizer
================

Create such a random number generator that for :math:`n` calls it would return a unique
non-repeating random number between :math:`1` and :math:`n`.

"""
from random import randrange


class Randomizer:
    """Generator of non-repeating random numbers in a range.

    This generator maintains a partitioned cache of unused random numbers. On each invocation
    the number is picked from a partition of remaining unused slots.

    """

    def __init__(self, n):
        """Bound randomizer.

        :param n: The upper bound for the randomizer.

        """
        self.n = n
        self.q = 0  # Number of calls to the generator
        self.cache = [i + 1 for i in range(n)]

    def get_next(self):
        """Picks a number from remaining unused random numbers.

        :return: Next random number.

        """
        p = self.n - self.q  # Number of remaining unused slots in cache
        r = randrange(p)
        self._swap(self.q, self.q + r)
        x = self.cache[self.q]
        self.q += 1
        return x

    def _swap(self, a, b):
        """Swaps two elements in a cache.

        :param a: Index of a first element.
        :param b: Index of a second element.

        """
        self.cache[a], self.cache[b] = self.cache[b], self.cache[a]
