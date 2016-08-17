"""
The maximum subarray problem is the task of finding the contiguous subarray within a
 one-dimensional array of numbers which has the largest sum. For example, for the
 sequence of values `[−2, 1, −3, 4, −1, 2, 1, −5, 4]`; the contiguous subarray with the
 largest sum is `[4, −1, 2, 1]`, with sum 6.

Linear-time solution is named after Jay Kadane who first found it in 1984.
"""


def subarray(A):
    """
    Returns continuous sub-array with the maximum sum.

    Kadane's algorithm consists of a scan through the array values, computing at each
     position the maximum subarray ending at that position. The implied starting position
     is just after the last position at which the sum went negative.

    This algorithm can be viewed as a simple example of dynamic programming.

    Complexity: O(n)
    :param list[int] A: Input array
    :return list[int]: Maximum subarray
    """
    n = len(A)
    q = A[0]  # Maximum at current position
    m = A[0]  # Maximum seen so far
    l, r = 0, 1  # Left and right pointer of sub-array window
    m_l = 0  # Left pointer at the time last maximum was found
    for i in range(1, n):
        x = A[i]
        if q + x > x:
            q += x
        else:
            q = x
        if q > m:
            r = i + 1
            m = q
            m_l = l
        else:
            l = i + 1
    return A[m_l:r]


def max_sum(A):
    """
    Returns value of the maximum subarray sum.

    This is a simplified version of Kadane's algorithm that only returns the target sum.

    Complexity: O(n)
    :param list[int] A: Input array
    :return int: Maximum subarray sum
    """
    n = len(A)
    q = A[0]  # Maximum at current position
    m = A[0]  # Maximum seen so far
    for x in A[1:n]:
        q = max(x, q + x)
        m = max(m, q)
    return m
