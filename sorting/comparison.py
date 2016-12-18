def bubble_sort(A):
    """Sorts an array of objects in place using bubble sorting algorithm.

    Bubble Sort is considered one the most ineffective sorting methods. It makes *n* runs
    over the whole array. In every pass it iterates backwards over the yet-to-be-sorted
    part and repeatedly swaps neighbour elements that are out of order. As a result
    elements "bubble" up or down (depending on sorting direction) in the array.

    Complexity:
        Average/worst :math:`O(n^2)`. :math:`O(n)` if array is already sorted. Bubble sort
        is a stable in-place sorting algorithm.

    :param list A: Array to sort.
    :return: :data:`None`. Input array is mutated.

    """
    n = len(A)
    i_n = n - 1  # Index of last element
    for k in range(0, i_n):
        for i in range(i_n, k, -1):
            if A[i] < A[i - 1]:  # Flip this comparison for reversed order
                A[i], A[i - 1] = A[i - 1], A[i]


def heap_sort(A):
    """Sorts an array of objects in place using heap sorting algorithm.

    Heap Sort takes an advantage of one of the main properties of the max-heap, that is
    that the max element is always at the top of the heap. For more information about the
    max-heap data structure, see trees/max_heap.

    Heap sort is performed in-place, and :func:`max_heapify()` is applied to a reduced
    subset of an input array after each iteration. Heap sort is one of the most optimal
    sorting algorithms using comparison model.

    Complexity:
        :math:`O(n \log n)`. Heap Sort is not stable, its runtime depends on the
        implementation of the heap. Heap is built in :math:`n` time, each of :math:`n-1`
        calls to heapify function takes :math:`\log n`.

    :param list A: Array to sort.
    :return: :data:`None`. Input array is mutated.

    """
    from basic_data_structures.heaps.max_heap import build_max_heap
    from basic_data_structures.heaps.max_heap import max_heapify

    n = len(A)
    i_n = n - 1  # Index of a last element
    build_max_heap(A)
    for i in range(i_n, 0, -1):
        # Stash top element at the end of the array, replace top element with
        # the one at the bottom of the heap.
        A[0], A[i] = A[i], A[0]
        # Elements below `i` are stashed in a sorted order.
        max_heapify(A, 0, i)  # Fix the still heapified, reduced by 1, subset of `A`


def insertion_sort(A):
    """Sorts an array of objects in place using insertion sorting algorithm.

    Insertion Sort traverses the list starting with a second element and assumes that items
    to the left of the pointer are already sorted. It "picks" the next element to the right
    of the pointer and puts it in its position in the sorted part of an array, iteratively
    comparing it with previous elements. The best analogy for insertion sort is sorting a
    hand of cards.

    Insertion Sort generally shows good performance on small number of elements due to less
    constant-time operations (compared to merge sort, for example).

    Complexity:
        Best :math:`O(n)`. Average/worst :math:`O(n^2)`. Insertion Sort is stable, swaps
        elements in place and does not require additional storage.

    :param list A: Array to sort.
    :return: :data:`None`. Input array is mutated.

    """
    n = len(A)
    for k in range(1, n):
        v = A[k]  # Value of a picked element
        i = k  # Index of a picked element
        while i > 0 and A[i - 1] > v:  # Flip this comparison for reversed order
            A[i] = A[i - 1]
            i -= 1
        A[i] = v
