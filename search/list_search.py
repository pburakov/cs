from abstract_data_types.linked_list import OrderedList
from abstract_data_types.linked_list import UnorderedList


def sequential_search(list, needle, ordered=False):
    """
    Brute force iteration search. For explanation, see linked list search.
     Note: average and worst case is faster for an Ordered list.
    """
    if ordered is True:
        linked_list = OrderedList()
    else:
        linked_list = UnorderedList()
    for i in list:
        linked_list.add(i)
    return linked_list.search(needle)


def binary_search(ordered_list, needle):
    """
    Divide-and-conquer search algorithm, works ONLY for ordered lists. It is very
     similar to a Binary Tree Search. Determines in which part of the list
     Needle is located by checking midpoint value and gradually reducing the
     search window by moving Left and Right marker indexes.
    """
    left = 0
    right = len(ordered_list) - 1
    while left <= right:
        midpoint = (left + right) // 2
        if ordered_list[midpoint] == needle:
            return True
        else:
            if needle < ordered_list[midpoint]:
                right = midpoint - 1
            else:
                left = midpoint + 1
    return False


def binary_rec_search(ordered_list, needle):
    """
    Recursive version of a Binary Search. List is being split to smaller pieces
     and each chunk is then recursively searched based on anticipated item index.
    Works ONLY for ordered lists.
    """
    if len(ordered_list) == 0:
        return False
    else:
        midpoint = len(ordered_list) // 2
        if ordered_list[midpoint] == needle:
            return True
        else:
            if needle < ordered_list[midpoint]:
                return binary_rec_search(ordered_list[:midpoint], needle)
            else:
                return binary_rec_search(ordered_list[midpoint + 1:], needle)


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
