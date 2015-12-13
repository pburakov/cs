def quick_sort(list):
    """
    Quick Sort is a recursive divide-and-conquer algorithm similar to Merge Sort,
     but not using additional storage. A Quick Sort first selects a pivot value
     (in this implementation it's the first element on the list), then it
     traverses the remaining partition by moving the left and right marker of
     the partition. While traversing quick sort keeps smaller values under the
     left marker and bigger value under the right marker, swapping their positions
     if needed. Markers move towards the future position of a Pivot Value which
     is called the Split Point. The the operation then is repeated recursively
     for both halves to the left and to the right of the Split point.
    Complexity: best/average O(n log(n)), worst O(n^2)
    """
    qs_helper(list, 0, len(list) - 1)


def qs_helper(list, first, last):
    if first < last:
        split_point = partition(list, first, last)
        print('split point is', split_point)
        qs_helper(list, first, split_point)
        qs_helper(list, split_point + 1, last)


def partition(list, first, last):
    print('partition [', first, '-', last, ']')
    pivot_value = list[first]
    l_marker = first + 1
    r_marker = last
    while r_marker >= l_marker:
        while l_marker <= r_marker and list[l_marker] <= pivot_value:
            l_marker += 1

        while list[r_marker] >= pivot_value and r_marker >= l_marker:
            r_marker -= 1

        if r_marker < l_marker:
            break
        else:
            print(' swapping', list[l_marker], 'and', list[r_marker])
            list[l_marker], list[r_marker] = list[r_marker], list[l_marker]
    print(' swapping', list[first], 'and', list[r_marker])
    list[first], list[r_marker] = list[r_marker], list[first]
    return r_marker
