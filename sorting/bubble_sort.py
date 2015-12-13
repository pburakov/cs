def bubble_sort(list):
    """
    Bubble Sort makes n passes from end to start and swaps neighbour elements
     if inconsistency is found. Bubble Sort is considered one the most ineffective
     sorting methods along with Selection Sort as it makes same amount of passes
     for every element of a list, uses nested loops and makes several swaps
     per pass.
    Complexity: best O(n), average/worst O(n^2)
    """
    for pass_num in range(len(list) - 1, 0, -1):
        print('pass', abs(pass_num - len(list)))
        for i in range(pass_num):
            if list[i] > list[i + 1]:
                print(' swapped', list[i], 'and', list[i + 1])
                list[i], list[i + 1] = list[i + 1], list[i]
