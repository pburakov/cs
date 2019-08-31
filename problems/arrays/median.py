"""
Median of Two Sorted Arrays
===========================

There are two sorted arrays :math:`A` and :math:`B` of size :math:`m` and :math:`n`
respectively. Find the median of the two sorted arrays if arrays :math:`A` and :math:`B` were
merged.

Example::

    (A=[1, 4, 5], B=[2, 3]) -> 3

This problem is discussed in more detail in this tutorial:
https://www.youtube.com/watch?v=LPFhl65R7ww.

"""


def median(A, B):
    """Computes a median of two sorted arrays.

    The key to the solution is to partition two arrays in two parts. All elements combined in
    the left partition are less than the elements in the right partition. We use binary search
    on a smaller array to find such partition.

    A few important observations:

        - If we take :math:`x` elements from the first array to our left part, it means that
          we need to take :math:`\\frac{m+n+1}{2}-x` elements from the second array.
        - The biggest element in the left part of the first array should be less than the
          minimum element of the right part of the second array.
        - The biggest element of the left part of the second array should be less than the
          minimum element of the right part of the first array.

    If we don't find the right partition we continue our search, adjusting boundaries
    accordingly.

    Complexity:
        :math:`O(\log{m+n})`.

    :param list A: Input array.
    :param list B: Input array.
    :return: Median of merged input arrays.

    """
    m, n = len(A), len(B)
    if m > n:
        return median(B, A)
    l, r = 0, m
    while l <= r:
        p_a = l + r // 2  # Partition in array A
        p_b = (m + n + 1) // 2 - p_a  # Partition in array B

        max_left_a = -inf if p_a == 0 else A[p_a - 1]
        min_right_a = inf if p_a == len(A) else A[p_a]
        max_left_b = -inf if p_b == 0 else B[p_b - 1]
        min_right_b = inf if p_b == len(B) else B[p_b]

        if max_left_a <= min_right_b and max_left_b <= min_right_a:
            if (m + n) % 2 == 0:
                return (max(max_left_a, max_left_b) + min(min_right_a, min_right_b)) / 2.0
            else:
                return float(max(max_left_a, max_left_b))
        elif max_left_a > min_right_b:
            r = p_a - 1
        else:
            l = p_a + 1
    return None


inf = float("inf")
