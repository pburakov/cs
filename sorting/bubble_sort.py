def bubble_sort(list):
    """
    Bubble Sort makes n passes from end to start and swaps neighbour elements
     if inconsistency is found. Element "bubble" up or down (depending on sorting
     direction) in the list.

    Bubble Sort is considered one the most ineffective sorting methods along with
     Selection Sort.

    Complexity: average/worst O(n^2)
    """
    for k in range(len(list) - 1):
        for i in range(len(list) - 1):
            if list[i] < list[i + 1]:
                print(' swapped', list[i], 'and', list[i + 1])
                list[i + 1], list[i] = list[i], list[i + 1]
    return list
