"""
 TODO: Add description here
"""

from trees.max_heap import build_max_heap
from trees.max_heap import max_heapify

def heap_sort(A):
    P = []       # Product of the heap sort
    n = len(A)   # Length of an array
    i_n = n - 1  # Index of a last element

    build_max_heap(A)

    for i in range(i_n, -1, -1):
        P.append(A[0])           # Take the max element of a max-heap
        A[0], A[i] = A[i], A[0]  # Exchange it with the bottom one
        del A[i]                 # It's no longer needed

        # Fix the reduced heap with the lowest element on top
        max_heapify(A, 0)

    return P
