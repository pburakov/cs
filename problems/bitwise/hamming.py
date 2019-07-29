"""
Pairwise Hamming Distance
=========================

In information theory, the Hamming distance between two strings of equal length is the number
of positions at which the corresponding symbols are different. In other words, it measures the
minimum number of substitutions required to change one string into the other. For example, for
:math:`1011101_2` and :math:`1001001_2`, Hamming distance :math:`H=2`. The minimum Hamming
distance is used to define some essential notions in coding theory, such as error detecting
and error correcting codes.

Given an array :math:`A` of :math:`n` non-negative integers, find the sum of hamming distances
of all pairs of integers in the array.

Examples::

    h([2, 7]) -> 2     # A=(010),(111)
    h({1, 3, 5}) -> 8  # A=(001,011,101)

Assume all elements in :math:`A` are 32 integers.

"""


def solution(A):
    """Computes the sum of Hamming distances for all pairs in the set.

    Hamming distance can only be computed for terms of equal lengths.

    Suppose the given array contains only binary numbers, either 1 or 0. Let :math:`x` be the
    number of 0-elements and :math:`y` be the number of 1-elements. The sum of Hamming
    distances of all pairs will be :math:`2xy`. Every pair containing one element from
    :math:`x` and one element from :math:`y` will contribute :math:`1` to the sum.

    Our array contains numbers of 32 bits. Instead of traversing the elements, we can traverse
    the bit positions. For example, in set :math:`A=\{2,4,6\}=\{010_2,100_2,110_2\}`, from
    least significant bit to most significant bit we count :math:`x_1=3,y_1=0,x_2=1,y_2=2,
    x_3=1,y_3=2`, hence the sum is :math:`S=(2\\times3\\times0)+(2\\times1\\times2)
    +(2\\times1\\times2) = 8`.

    Complexity:
        :math:`O(n)`, or :math:`\\theta(32n)` on a tighter bound.

    :param list[int] A: Input set, with each element length 32 bits maximum.
    :return: Sum of Hamming distances.

    """
    n = len(A)
    S = 0
    for i in range(32):  # max 32 bits
        M = 1 << i  # bit mask
        x = 0
        for a in A:
            if M & a:
                x += 1
        y = n - x
        S += 2 * x * y
    return S
