def selection_sort(list):
    """
    Selection Sort finds the biggest element in the search window (limited by
     a starting element and a Right position marker) and swaps it with an element
     at the Right edge of the search window. One of the least effective search
     algorithms with constant complexity of O(n^2) in all cases.
    """
    for r_marker in range(len(list) - 1, 0, -1):
        i_max = 0  # index of a maximum value
        for i in range(1, r_marker):
            if list[i] > list[i_max]:
                i_max = i
        print('marker at', r_marker, ': swapped', list[r_marker], 'and', list[i_max])
        list[r_marker], list[i_max] = list[i_max], list[r_marker]
