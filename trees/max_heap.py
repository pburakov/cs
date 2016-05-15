"""
Binary Heap is a basic implementation of a Priority Queue. Because heap is represented
 as a nearly complete Binary Tree, is is usually implemented as an array (or a list
 in Python).

Given that the first index of a tree starts at `0`, the index of every child
 Node in a Binary Heap can be computed as `i * 2 + 1` for left child and `i * 2 + 2`
 for the right child (or root at `1`, `i * 2` and `i * 2 + 1` for children
 respectively, as presented in CLRS).

Another important properties of a Binary Heap determine its main uses and common
 variations: max-heap and min-heap. For max-heap, every element is bigger than
 its children and it has the biggest element at the root thus giving the constant
 time O(1) for the max() operation. Heap properties must be maintained throughout
 any modification made to it.
"""


def max_heapify(A, i):
    """
    Rearranges array `A` "below" index `i` maintaining max-heap properties. Assumes
     that binary trees rooted at indexes `l` and `r` (children of `A[i]`) are max-
     heaps but that A[i] might violate max-heap property of being larger element.
    :return: None. List `A` is mutated.
    """
    n = len(A)      # Heap size
    l = 2 * i + 1   # Index of a left child
    r = 2 * i + 2   # Index of a right child
    i_largest = i   # Index of a largest element (`i` by default)

    if l < n and A[l] > A[i]:
        i_largest = l
    if r < n and A[r] > A[i_largest]:
        i_largest = r
    if i_largest != i:
        A[i], A[i_largest] = A[i_largest], A[i]
        max_heapify(A, i_largest)  # Repeat one level down
    else:
        pass                       # No changes


def build_max_heap(A):
    """
    Rearranges list `A` into a representation of a max-heap, ensuring that the heap
     properties are maintained.
    :return: None. List `A` is mutated.
    """

    i_n = len(A) - 1  # Index of a last element
    i_n_2 = i_n // 2  # Index of last element's parent

    for i in range(i_n_2, -1, -1):
        max_heapify(A, i)
