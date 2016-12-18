"""
Three Sum
=========

Find integer triplets in an array with the sum of 0.

Example::

    Input: [1, -6, 3, 8, -2, 2] -> sort -> [-6, -2, 1, 2, 3, 8]
    Output: (-6, -2, 8)

"""


def solution(A):
    """Finds integers triplets in an array with the sum of zero.

    First two pointers go forward one after another and third one traverses array backwards.
    An array has to be sorted first in order to correctly find all possible solutions and
    break the traversal when no further solution can be found.

    This solution has interesting approach to iterating the array using three pointers in
    quadratic time.

    Complexity:
        :math:`O(n^2)`.

    :param list[int] A: Input array.
    :return: List of output integer triplets.

    """
    n = len(A)
    P = []
    if n < 3:
        return P
    A.sort()  # Any sorting algorithm better than O(n^2)
    for i in range(0, n - 2):  # First pointer
        if i == 0 or A[i] > A[i - 1]:
            j = i + 1  # Second pointer
            k = n - 1  # Third pointer
            while j < k:
                if A[i] + A[j] + A[k] == 0:
                    P.append((A[i], A[j], A[k]))
                    j += 1
                    k -= 1
                    while j < k and A[j] == A[j - 1]:
                        j += 1
                    while j < k and A[k] == A[k + 1]:
                        k -= 1
                elif A[i] + A[j] + A[k] < 0:
                    j += 1
                else:
                    k -= 1
    return P
