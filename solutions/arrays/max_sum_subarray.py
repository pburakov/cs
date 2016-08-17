def max_sum(A):
    """
    Returns maximum sum value.

    :param list[int] A:
    :return int:
    """
    n = len(A)
    q = A[0]  # Starting maximum value
    m = A[0]  # Maximum seen so far
    for x in A[1:n]:
        q = max(x, q + x)
        m = max(m, q)
    return m


def subarray(A):
    """
    Returns continuous sub-array with the maximum sum.

    :param list[int] A:
    :return int:
    """
    n = len(A)
    q = A[0]  # Starting maximum value
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
