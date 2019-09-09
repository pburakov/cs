"""
Bloom Filter
============

A Bloom filter is a space-efficient probabilistic data structure that allows to test whether an element is a member of a set. False positive matches are possible, but false negatives are not – in other words, a query returns either "possibly in set" or "definitely not in set".

The filter was conceived by Burton Howard Bloom in 1970.
"""

import math

from numerical.hashing import h_multiplication


class BloomFilter:
    def __init__(self, n, p):
        """

        :param int n:
        :param float p:

        """
        # The size of a bit array
        m = int(-(n * math.log(p)) / (math.log(2) ** 2))
        self.A = [0] * m  # Bit array
        self.m = m

        # The number of hash functions to use
        k = int((m / n) * math.log(2))
        self.k = k


def filter_insert(F, x):
    """

    :param BloomFilter F:
    :param int x:

    """
    for i in range(0, F.k):
        d = h_multiplication(x + i, F.m)
        F.A[d] = 1  # Toggle bit


def filter_check(F, x):
    """

    :param BloomFilter F:
    :param int x:
    :return:
    """
    for i in range(0, F.k):
        d = h_multiplication(x + i, F.m)
        if F.A[d] is 0:
            return False
    return True
