def bubble_sort(A):
    """
    Sort an array of objects in place using bubble sorting algorithm.

    Bubble Sort repeatedly swaps neighbour elements that are out of order. Elements
     "bubble" up or down (depending on sorting direction) in the list.

    Original Bubble Sort is considered one the most ineffective sorting methods.
     Below is slightly "optimized" version of the algorithm that iterates backwards
     over the unsorted part, that is similar to Insertion sort.

    Complexity: best O(n), average/worst O(n^2). Bubble sort is a stable algorithm
     and performs in-place sorting.
    :param list A: Array (list) to sort
    :return None: List `A` is mutated.
    """
    n = len(A)
    i_n = n - 1  # Index of last element
    for k in range(0, i_n):
        for i in range(i_n, k, -1):
            if A[i] < A[i - 1]:  # Flip this comparison for reversed order
                A[i], A[i - 1] = A[i - 1], A[i]
