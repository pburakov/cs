def selection_sort(list):
    """
    Selection Sort is a "child's algorithm". It finds the smallest / biggest element
     in the search window and swaps it with an element in the front. One of the
     least effective search algorithms.

    Complexity: O(n^2) in all cases.
    """

    for i in range(len(list)):
        for k in range(len(list)):
            if list[k] > list[i]:
                print('swapped', list[i], 'and', list[k])
                list[i], list[k] = list[k], list[i]
    return list
