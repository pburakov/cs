from sorting.insertion_sort import insertion_sort
from sorting.merge_sort import merge_sort
from sorting.heap_sort import heap_sort

l = [4, 7, 5, 2, 3, 9, 6, 1, 8]

# Insertion Sort sorts array in place and has no output
insertion_sort(l)
print(l)

l = [4, 7, 5, 2, 3, 9, 6, 1, 8]
# Merge Sort yields a new array
print(merge_sort(l))

l = [4, 7, 5, 2, 3, 9, 6, 1, 8]
# Heap Sort performs in place sorting
heap_sort(l)
print(l)
