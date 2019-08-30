"""
Shifted Array Search
====================

A sorted array of distinct integers :math:`A` is shifted to the left by an unknown offset
and you don’t have a pre-shifted copy of it. For instance, the sequence
:math:`A'=\{1, 2, 3, 4, 5\}` becomes :math:`A=\{3, 4, 5, 1, 2\}`, after shifting it twice to
the left. Given :math:`A` and an integer :math:`x`, implement a function that finds and
returns the index of :math:`x` in :math:`A`. Assume that the offset can be any value between
:math:`0` and :math:`|A| - 1`.

Example::

    (A=[9, 12, 17, 2, 4, 5], x=2) -> 3

"""


def shifted_array_search(A, x):
    """Finds a number in a shifted sorted array.

    The optimal solution uses a modified binary search routine to first find an index of a
    pivot, then a regular binary search to find the target element :math:`x`.

    Complexity:
        :math:`O(\log n)` for sequential binary searches.

    :param list A: Input array.
    :param int x: Target element.
    :return: Index of target number in the array.

    """
    pivot = find_pivot(A)
    if pivot == 0 or x < A[0]:
        return bin_search(A, x, l=pivot, r=len(A) - 1)
    else:
        return bin_search(A, x, l=0, r=pivot - 1)


def find_pivot(A):
    """Modified binary search routine for finding a pivot index in a shifted array.

    Same as regular binary search, but compares middle element with element at the rightmost
    edge to detect the order discrepancy.

    Complexity:
        :math:`O(\log n)`.

    :param list A: Sorted shifted array.
    :return: Index of the pivot point.

    """
    l = 0
    r = len(A) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if mid == 0 or A[mid] < A[mid - 1]:
            return mid
        elif A[mid] > A[0]:
            l = mid + 1
        else:
            r = mid - 1
    return 0


def bin_search(A, x, l, r):
    """Basic binary search routine.

    Complexity:
        :math:`O(\log n)`.

    :param list A: Input array.
    :param int x: Target element.
    :param int l: Lower bound index.
    :param int r: Upper bound index.
    :return: Index of target number in the array or :data:`None`, if not found.

    """
    while l <= r:
        mid = l + (r - l) // 2
        if A[mid] < x:
            l = mid + 1
        elif A[mid] == x:
            return mid
        else:
            r = mid - 1
    return None
