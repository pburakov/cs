def sort(A, k):
    """
    Sort k-messed array.

    There's an obvious regular sort with `O(n log(n))` complexity or even `O(nk)` solution
     to this problem, however we can do better. We use heap to extract the minimum as we
     shift the `k`-sized window from the beginning to the end.

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
