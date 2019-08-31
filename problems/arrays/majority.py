"""
Majority Element
================

In an array of comparable objects (e.g. integers), find the majority element. If :math:`n`
is the size of the array, majority element is an element that occurs at least
:math:`\\lfloor n/_2 \\rfloor` times in the array. Return :data:`None` if no majority
element is present.

Example::

    [1, 2, 2, 3, 2] -> 2
    [5, 2, 1, 4, 2] -> None

The algorithm should use constant space.
"""


def majority(A):
    """Finds majority element in the list.

    This solution implements Moore’s Voting Algorithm which is a two step process. First we
    get an element occurring most of the time in the array. By counting, we evaluate if our
    candidate is supported with more occurring elements. We reset the counter if it went
    below zero.

    Statistically, the first step may give us a false positive. On the second step, we check
    if the element is in fact a majority element.

    Complexity:
        :math:`O(n)`, no extra space is used.

    :param list[object] A: Input list.
    :return: Majority element or :data:`None` if not found.

    """
    c = 0  # Candidate index
    count = 1
    n = len(A)
    for i in range(1, n):
        if A[c] == A[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            c = i
            count = 1
    candidate = A[c]
    count = 0
    for a in A:
        if a == candidate:
            count += 1
    if count >= n / 2:
        return candidate
    else:
        return None
