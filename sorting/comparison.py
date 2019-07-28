"""
Comparison Sorting Algorithms
=============================
"""
from basic.heaps import build_max_heap, max_heapify


def bubble_sort(A):
    """Sorts an array in place using bubble sort algorithm.

    Bubble Sort is considered one the most ineffective sorting methods. It makes *n* runs
    over the whole array. In every pass, it iterates backwards over the yet-to-be-sorted
    part and repeatedly swaps neighbour elements that are out of order. As a result,
    the elements "bubble" up or down (depending on sorting direction) in the array.

    Bubble sort is a stable sorting algorithm.

    Complexity:
        Average/worst :math:`O(n^2)`. :math:`O(n)` if the array is already sorted.

    :param list A: Array to sort.

    """
    n = len(A)
    i_n = n - 1  # Index of last element
    for k in range(0, i_n):
        for i in range(i_n, k, -1):
            if A[i] < A[i - 1]:  # Flip this comparison for reversed order
                A[i], A[i - 1] = A[i - 1], A[i]


def heap_sort(A):
    """Sorts an array in place using heap sort algorithm.

    Heap Sort takes advantage of the main property of a max-heap, which state that the max
    element is always at the top of the heap. Heap sort is one of the most optimal sorting
    algorithms using a comparison model.

    Heap Sort is not a stable sorting algorithm.

    Complexity:
        :math:`O(n \log n)`, the runtime depends on the implementation of the heap.

    :param list A: Array to sort.

    """
    n = len(A)
    i_n = n - 1  # Index of a last element
    build_max_heap(A)
    for i in range(i_n, 0, -1):
        # Stash top element at the end of the array, replace top element with
        # the one at the bottom of the heap.
        A[0], A[i] = A[i], A[0]
        max_heapify(A, 0)  # Let top element sink down to its place in the heap


def insertion_sort(A):
    """Sorts an array in place using insertion sort algorithm.

    Insertion Sort traverses the list starting with a second element and assumes that items
    to the left of the pointer are already sorted. It "picks" the next element at the right
    side of the pointer and puts it in its position in the sorted part of an array. The best
    analogy for insertion sort is sorting a hand of cards.

    Insertion Sort generally shows good performance on a small number of elements due to
    fewer constant-time operations.

    Insertion sort is a stable sorting algorithm.

    Complexity:
        Best :math:`O(n)`. Average/worst :math:`O(n^2)`.

    :param list A: Array to sort.

    """
    n = len(A)
    for k in range(1, n):
        v = A[k]  # Value of a picked element
        i = k  # Index of a picked element
        while i > 0 and A[i - 1] > v:  # Flip this comparison for reversed order
            A[i] = A[i - 1]
            i -= 1
        A[i] = v
