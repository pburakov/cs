def insertion_sort(A):
    """
    Sort an array of objects in place using insertion sorting algorithm.

    Insertion Sort traverses the list starting with a second element and assumes
     that items to the left of the pointer are already sorted. It "picks" the next
     element to the right of the pointer and puts it in its position in the sorted
     part of an array, iteratively comparing it with previous elements. The best
     analogy for insertion sort is sorting a hand of cards.

    Insertion Sort generally shows good performance on small number of elements due
     to less constant-time operations (compared to merge sort, for example).

    Complexity: best O(n), average/worst O(n^2). Insertion Sort is stable, swaps
     elements in place and does not require additional storage.
    :param list A: Array (list) to sort
    :return None: List `A` is mutated.
    """
    n = len(A)
    for k in range(1, n):
        v = A[k]  # Value of a picked element
        i = k     # Index of a picked element
        while i > 0 and A[i - 1] > v:  # Flip this comparison for reversed order
            A[i] = A[i - 1]
            i -= 1
        A[i] = v
