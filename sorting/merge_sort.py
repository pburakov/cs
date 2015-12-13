def merge_sort(list):
    """
    Merge sort is a recursive sorting algorithm that continually spits a list in
     half. If the list is empty or has one item it is sorted by definition (the
     base case), otherwise the list is split and Merge sort is invoked recursively
     on both halves. Once the two halves are sorted, the fundamental Merge operation
     is performed. This operation places the items back into the original list one
     at a time by repeatedly taking the smallest item for the sorted lists.
    Complexity: O(n log(n)) in all cases. Log(n) for splitting, n for merge.
     Merge Sort requires additional memory to hold the sliced two halves which can
     be critical for larger sets.
    """
    print('split', list)
    if len(list) > 1:
        midpoint = len(list) // 2
        left_half = list[:midpoint]
        right_half = list[midpoint:]
        merge_sort(left_half)
        merge_sort(right_half)
        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                list[k] = left_half[i]
                i += 1
            else:
                list[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            list[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            list[k] = right_half[j]
            j += 1
            k += 1
    print('merged', list)
