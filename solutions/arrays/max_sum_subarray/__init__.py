def subarray(A):
    """
    Returns continuous sub-array with the maximum sum.

    Kadane's algorithm consists of a scan through the values in the array, computing at
     each position the maximum subarray ending at that position. The implied starting
     position is just after the last position at which the sum went negative.

    This algorithm can be viewed as a simple example of dynamic programming.

    Complexity: O(n)
    :param list[int] A: Input array
    :return list[int]: Maximum subarray
    """
    # TODO: Fails on some cases (fix)
    n = len(A)
    p = A[0]  # Maximum at current position
    q = A[0]  # Maximum seen so far
    l, r = 0, 1  # Left and right pointer of sub-array window
    m_l = 0  # Left pointer at the time last maximum was found
    for i in range(1, n):
        x = A[i]
        if p + x > x:
            p += x
        else:
            p = x
        if p > q:
            r = i + 1
            q = p
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
    p = A[0]  # Maximum at current position
    q = A[0]  # Maximum seen so far
    for x in A[1:n]:
        p = max(x, p + x)
        q = max(q, p)
    return q
