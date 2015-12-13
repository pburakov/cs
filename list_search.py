from search.list_search import sequential_search
from search.list_search import binary_search
from search.list_search import binary_rec_search

import time

# Sequential Search
start_time = time.clock()
print(sequential_search([9, 1, 7, 8, 5, 2], 5))  # True
print(sequential_search([9, 8, 7, 6, 5, 4], 3))  # False
print(" time: %6.6f" % (time.clock() - start_time))

# Binary Search
start_time = time.clock()
print(binary_search([1, 3, 7, 8, 9, 10, 25], 9))  # True
print(binary_search([1, 3, 7, 8, 9, 10, 25], 11))  # False
print(" time: %6.6f" % (time.clock() - start_time))

# Recursive Binary Search
start_time = time.clock()
print(binary_rec_search([1, 3, 7, 8, 9, 10, 26], 9))  # True
print(binary_rec_search([1, 3, 7, 8, 9, 10, 26], 11))  # False
print(" time: %6.6f" % (time.clock() - start_time))
