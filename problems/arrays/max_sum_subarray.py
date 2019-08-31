"""
Maximum Sum Subarray
====================

The maximum subarray problem is the task of finding the maximum sum that can be yielded
from contiguous subarray within a one-dimensional array of numbers.

Example::

    [-2, 1, -3, 4, -1, 2, 1, -5, 4] -> 6  # [4, -1, 2, 1]

Linear-time solution is named after Jay Kadane who first found it in 1984.
"""


def max_sum_subarray(A):
    """Returns value of the maximum subarray sum.

    This is a simplified version of Kadane's algorithm that returns the target sum.

    Complexity:
        :math:`O(n)`.

    :param list[int] A: Input array.
    :return: Maximum subarray sum.

    """
    n = len(A)
    p = A[0]  # Maximum at current position
    q = p  # Maximum seen so far
    for x in A[1:n]:
        p = max(x, p + x)
        q = max(q, p)
    return q


def max_sum_subarray_adv(A):
    """Adaptation of Kadane's algorithm, returning subarray boundaries.

    Right boundary is exclusive (Python range style).

    Complexity:
        :math:`O(n)`.

    :param list[int] A: Input array.
    :return: Tuple of max subarray window index boundaries.

    """
    n = len(A)
    p = A[0]
    q = p
    l, r = 0, 1  # Window boundaries
    ml, mr = l, r  # Maximum window boundaries
    for i in range(1, n):
        v = A[i]
        if v > p + v:  # New max, reset window
            p = v
            l = i
            r = i + 1
        else:  # Add to sum, extend window right
            p = p + v
            r = i + 1
        if p > q:
            q = p
            ml, mr = l, r
    return ml, mr
