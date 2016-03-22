def quick_sort(list):
    """
    Quick Sort is a recursive divide-and-conquer algorithm similar to Merge Sort,
     but not using additional storage. A Quick Sort first selects a pivot point
     (in this implementation it's the first element of the list), splits the list and
     traverses two parts of the list keeping smaller elements to the left and bigger
     elements to the right of the pivot point.

    Complexity: best/average O(n log(n)), worst O(n^2)
    """
    if not list:
        return []
    else:
        pivot = list[0]
        less = [x for x in list if x < pivot]
        more = [x for x in list[1:] if x >= pivot]
        return quick_sort(less) + [pivot] + quick_sort(more)
