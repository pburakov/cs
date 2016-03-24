def quick_sort(list):
    """
    Quick Sort is a recursive divide-and-conquer algorithm similar to Merge Sort,
     but not using additional storage. A Quick Sort first selects a pivot point
     (in this implementation it's the value of first element of the list), then
     partitions the list and traverses two parts of the list keeping elements
     smaller than the pivot point to the left and elements bigger than the pivot
     point to the right.

    Complexity: best/average O(n log(n)), worst O(n^2)
    """
    if not list:
        return []
    else:
        print('got', list, end=', ')
        if len(list) == 1:
            print('1 elem. skiping')
            return list
        pivot = list[0]
        print('pivot point', pivot)
        less = [x for x in list if x < pivot]
        print('less:', less)
        greater = [x for x in list[1:] if x >= pivot]
        print('greater or eq:', greater)
        return quick_sort(less) + [pivot] + quick_sort(greater)
