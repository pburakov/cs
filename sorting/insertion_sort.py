def insertion_sort(list):
    """
    Insertion Sort traverses the list starting with a second element and assumes
     that items to the left of the pointer are already sorted. It "picks" the next
     element to the right of the pointer and puts it in its position in the sorted
     part of an array, iteratively comparing it with previous elements. The best
     analogy for insertion sort is sorting a hand of cards.

    Insertion Sort generally shows good performance on small number of elements due
     to lesser constant-time operations (compared to merge sort, for example).

    Complexity: best O(n), average/worst O(n^2). Insertion Sort swaps elements in
     place and does not require additional storage.
    """

    n = len(list)
    for k in range(1, n):
        v = list[k]  # Value of a picked element
        i = k        # Index of picked element

        while i > 0 and list[i - 1] > v:  # Flip this comparison for reversed order
            list[i] = list[i - 1]
            i -= 1
        list[i] = v

    return list
