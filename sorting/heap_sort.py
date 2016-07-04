from basic_data_structures.heaps.max_heap import build_max_heap
from basic_data_structures.heaps.max_heap import max_heapify


def heap_sort(A):
    """
    Sort an array of objects in place using heap sorting algorithm.

    Heap Sort takes an advantage of one of the main properties of the max-heap,
     that is that the max element is always at the top of the heap. For more
     information about the max-heap data structure, see trees/max_heap.

    Heap sort is performed in-place, and `max_heapify()` is applied to a reduced
     subset of an array `A` after each iteration. Heap sort is one of the most optimal
     sorting algorithms using comparison model.

    Complexity: O(n log(n)). Heap Sort is not stable, its runtime depends on the
     implementation of the heap. Heap is built in `n` time, each of `n-1` calls to 
     heapify function takes `log(n)`.
    :param list A: Array (list) to sort
    :return None: List `A` is mutated.
    """
    n = len(A)
    i_n = n - 1  # Index of a last element
    build_max_heap(A)
    for i in range(i_n, 0, -1):
        # Stash top element at the end of the array, replace top element with
        # the one at the bottom of the heap.
        A[0], A[i] = A[i], A[0]
        # Elements below `i` are stashed in a sorted order.
        max_heapify(A, 0, i)  # Fix the still heapified, reduced by 1, subset of `A`
