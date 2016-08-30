"""
Given an array `A` of length `n` where each element is at most `k > 1` places away from
 its sorted position, plan and code an efficient algorithm to sort `A`.

Example: With `A=[3, 1, 2, 5, 4, 7, 6]` and `k=2` the element belonging to index 3 in the
 sorted array, may be at indices 4, 5, 6, 7 or 8 on the given array.
"""


def sort(A, k):
    """
    Sort k-messed array.

    There's an obvious regular sort with `O(n log(n))` complexity or even `O(nk)`
     solution to this problem, however we can do better if we use heap to extract the
     minimum at each step.

    Algorithm assumes that `k > 1`.

    Complexity: O(n log(k))
    :param list A: Input array (list)
    :param int k: Max "messiness" distance
    :return None: List `A` is updated
    """
    from basic_data_structures.heaps.min_heap import min_heap_insert, heap_extract_min

    n = len(A)
    H = []
    i = 0
    for i in range(0, k):  # O(k log(k))
        min_heap_insert(H, A[i])
    for i in range(0, n - k):
        A[i] = heap_extract_min(H)  # O(log k)
        min_heap_insert(H, A[i + k])  # O(log k)
    i += 1
    while i < n and len(H) > 0:  # Remaining elements
        A[i] = heap_extract_min(H)
        i += 1
