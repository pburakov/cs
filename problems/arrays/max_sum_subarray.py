"""
# Maximum Sum Subarray

The maximum subarray problem is the task of finding the maximum sum that can be yielded
 from contiguous subarray within a one-dimensional array of numbers. For example, for the
 sequence of values `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`; such contiguous subarray is
 `[4, -1, 2, 1]`, with the sum `6`.

Linear-time solution is named after Jay Kadane who first found it in 1984.
"""


def max_sum(A):
    """
    Returns value of the maximum subarray sum.

    This is a simplified version of Kadane's algorithm that returns the target sum.

    Complexity: O(n)
    :param list[int] A: Input array
    :return int: Maximum subarray sum
    """
    n = len(A)
    p = A[0]  # Maximum at current position
    q = p  # Maximum seen so far
    for x in A[1:n]:
        p = max(x, p + x)
        q = max(q, p)
    return q
