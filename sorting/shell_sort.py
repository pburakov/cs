def shell_sort(list):
    """
    Shell Sort is similar to Insertion Sort, only uses Gaps instead of regular
     single step traversal. Each pass produces "more sorted" list. That makes
     the final pass efficient and makes Shell Sort slightly more effective
     than Insertion Sort.
    Complexity: best O(n) average/worst O(nlog(n)^2)
    """
    gap = len(list) // 2
    while gap > 0:
        for start in range(gap):
            print('Pass', start + 1)
            gap_insertion_sort(list, start, gap)
            gap //= 2


def gap_insertion_sort(list, start, gap):
    if gap == 0:
        start = 0
        gap = 1
    for marker in range(start + gap, len(list), gap):
        cur_value = list[marker]
        cur_index = marker
        print(' pos', marker, '->', cur_value)
        while cur_index >= gap and list[cur_index - gap] > cur_value:
            list[cur_index] = list[cur_index - gap]
            cur_index -= gap
        if cur_index != marker:
            print('  put before', list[cur_index])
        else:
            print('  put after', list[cur_index - gap])
        list[cur_index] = cur_value
