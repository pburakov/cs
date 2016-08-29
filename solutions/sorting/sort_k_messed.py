"""
Given an array `A` of length `n` where each element is at most `k > 1` places away from its sorted position, plan and code an efficient algorithm to sort `A`.

Example: With `A=[3, 1, 2, 5, 4, 7, 6]` and `k=2` the element belonging to index 3 in the sorted array, may be at indices 4, 5, 6, 7 or 8 on the given array.
"""
from basic_data_structures.heaps.min_heap import *


def sort(A, k):
    n = len(A)
    H = A[0:k]
    build_min_heap(H)
    i = 0
    for i in range(0, n - k):
        A[i] = heap_extract_min(H)
        min_heap_insert(H, A[i + k])
    i += 1
    while i < n and len(H) > 0:
        A[i] = heap_extract_min(H)
        i += 1
