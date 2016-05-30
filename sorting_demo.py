from sorting.insertion_sort import insertion_sort
from sorting.merge_sort import merge_sort
from sorting.heap_sort import heap_sort
from sorting.bubble_sort import bubble_sort
from sorting.counting_sort import counting_sort

l = [4, 7, 5, 2, 3, 9, 6, 1, 8]
insertion_sort(l)
print(l)

l = [4, 7, 5, 2, 3, 9, 6, 1, 8]
print(merge_sort(l))

l = [4, 7, 5, 2, 3, 9, 6, 1, 8]
heap_sort(l)
print(l)

l = [4, 7, 5, 2, 3, 9, 6, 1, 8]
bubble_sort(l)
print(l)

l = [4, 3, 1, 3, 2]
print(counting_sort(l, max(l)))
