"""
Hash Functions
==============

Hash function maps keys from the universe of all possible keys :math:`U` to a finite set of 
keys :math:`m`: :math:`h:U \\rightarrow \{ 0, 1, ..., m-1 \}`. Since mapping an infite set 
into a smaller finite set is impossible by definition, value **collisions** may occur. A 
hash function that does not result in collisions is called a **perfect hash function**. A 
property of a hash function that guarantees even distribution of values in the resulting 
set :math: `m` is called **hash function uniformity**. This property is used in hash tables.

Basic hash functions implemented here are vulnerable to collisions. The approach in which
a hash function ia chosen randomly from a family of functions :math:`\\mathcal{H}`
independently of the keys is called **universal hashing** (not implemented here).

Python's built-in hash function (`hash()`) supports encoding of any object to its hash 
value.
"""
import math


def h_division(k, m):
    """Hash function implemented using division method.

    When using the division method, we usually avoid certain values of :math:`m`, such as a
    power of 2. A large prime not too close to an exact power of 2 is often a good choice
    for :math:`m`, such as :math:`m = 701`.

    Complexity:
        :math:`O(1)`. Computation is fast due to a single division operation.

    :param int k: Input key.
    :param int m: Size of a table (total number of slots).
    :return: Hash value.

    """
    return k % m


def h_multiplication(k, m, A=(math.sqrt(5) - 1) / 2):
    """Hash function implemented using multiplication method.

    The multiplication method operates in two steps. First, we multiply the key :math:`k`
    by a constant A in the range :math:`0 < A < 1` and extract the fractional part of
    :math:`kA`. Then, we multiply this value by :math:`m` and take the floor of the result.
    In short, :math:`h(k) = \\lfloor m(kA\mod 1) \\rfloor`.

    An advantage of the multiplication method is that the value of :math:`m` is not
    critical. Although it works with any value of :math:`A` within the range, some values
    work better than others. Value :math:`A \\approx (\sqrt{5} - 1) / 2 = 0.6180339887...`
    was suggested by Knuth.

    Complexity:
        :math:`O(1)`.

    :param int k: Input key.
    :param int m: Size of a table (total number of slots).
    :param A: Constant in the range :math:`0 < A < 1`.
    :return: Hash value.

    """
    return math.floor(m * ((k * A) % 1))
