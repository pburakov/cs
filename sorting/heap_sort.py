"""
 Heap Sort takes an advantage of one of the main properties of the max-heap,
  that is that the max element is always at the top of the heap.

 For more information about the max-heap data structure, see trees/max_heap.

 Important note: This implementation uses additional storage yielding the product
  of the sort `P`. However, typical heap sort can be performed in-place, if
  `max_heapify()` is performed on a subset of an array `A`.

 Complexity: O(n log (n)). Heap Sort is not stable, its runtime depends on the
  implementation of the heap. Heap is typically build in n time, heapify function
  takes log(n) since the subset of `A` is reduced in each iteration.
"""

from trees.max_heap import build_max_heap
from trees.max_heap import max_heapify


def heap_sort(A):
    n = len(A)      # Length of an array
    P = [None] * n  # Product of the heap sort
    i_n = n - 1     # Index of a last element

    build_max_heap(A)
    for i in range(i_n, -1, -1):
        A[0], A[i] = A[i], A[0]  # Exchange top element with the bottom one
        # Stash the bottom element as part of a sorted subset whilst reducing
        # "heapified" portion of an array.
        P[i] = A.pop(i)
        # Fix the reduced heap with the lowest element on top
        max_heapify(A, 0)

    return P
