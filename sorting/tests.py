from sorting.shell_sort import shell_sort
from sorting.bubble_sort import bubble_sort
from sorting.insertion_sort import insertion_sort
from sorting.merge_sort import merge_sort
from sorting.selection_sort import selection_sort
from sorting.quick_sort import quick_sort

import time

l = [54, 26, 93, 17, 77, 31, 44, 55, 20, 105, 11]
print('Bubble Sort')
start_time = time.clock()
bubble_sort(l)
print("\ntime: %6.6f" % (time.clock() - start_time), end='\n\n')

l = [54, 26, 93, 17, 77, 31, 44, 55, 20, 105, 11]
print('Selection Sort')
start_time = time.clock()
selection_sort(l)
print("\ntime: %6.6f" % (time.clock() - start_time), end='\n\n')

l = [54, 26, 93, 17, 77, 31, 44, 55, 20, 105, 11]
print('Insertion Sort')
start_time = time.clock()
insertion_sort(l)
print("\ntime: %6.6f" % (time.clock() - start_time), end='\n\n')

l = [54, 26, 93, 17, 77, 31, 44, 55, 20, 105, 11]
print('Shell Sort')
start_time = time.clock()
shell_sort(l)
print("\ntime: %6.6f" % (time.clock() - start_time), end='\n\n')

l = [54, 26, 93, 17, 77, 31, 44, 55, 20, 105, 11]
print('Merge Sort')
start_time = time.clock()
merge_sort(l)
print("\ntime: %6.6f" % (time.clock() - start_time), end='\n\n')

l = [54, 26, 93, 17, 77, 31, 44, 55, 20, 105, 11]
start_time = time.clock()
print('Quick Sort')
quick_sort(l)
print("\ntime: %6.6f" % (time.clock() - start_time), end='\n\n')
