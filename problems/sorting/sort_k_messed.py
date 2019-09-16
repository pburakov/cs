"""
Sort K-messed Array
===================

Given an array :math:`A` of length :math:`n` where each element is at most :math:`k : k >
1` places away from its sorted position, plan and code an efficient algorithm to sort
:math:`A`. I.e. for :math:`A, k=2` final position of the element :math:`A_i, i=3` in the
sorted :math:`A'`, may be at indices :math:`i' \in \{1,2,3,4,5\}`.

Array must be sorted in place.

"""
from heapq import heappush, heappop


def sort(A, k):
    """Sort k-messed array.

    There's an obvious regular sort with :math:`O(n \log n)` complexity or even :math:`O(
    nk)` solution to this problem, however we can do better. We use heap to extract the
    minimum as we shift the :math:`k`-sized window from the beginning to the end.

    Algorithm works for `k > 1`.

    Complexity:
        :math:`O(n \log k)`.

    :param list A: Mutable input array.
    :param int k: Max "messiness" distance.

    """
    n = len(A)
    H = []
    i = 0
    for i in range(0, k):  # O(k log(k))
        heappush(H, A[i])
    for i in range(0, n - k):
        A[i] = heappop(H)  # O(log k)
        heappush(H, A[i + k])  # O(log k)
    i += 1
    while i < n and len(H) > 0:  # Remaining elements
        A[i] = heappop(H)
        i += 1
