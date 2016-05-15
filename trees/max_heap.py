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

Heap structure is useful when it is required to have fast access to the top element,
 however, the remainder of the array is kept partially unsorted.
"""


def max_heapify(A, i, n=None):
    """
    Rearranges array `A` "below" index `i` to maintain max-heap properties. It assumes
     that binary trees rooted at indexes `l` and `r` (children of `A[i]`) are max-
     heaps, but that A[i] might violate max-heap property of being larger element.
    This algorithm lets the value at `A[i]` "float-down" in the max-heap so that the
     subtree rooted at index `i` obeys the max-heap property.
    :param A: Array (list) to heapify
    :param i: Integer index of a root
    :param n: Optional integer length of the subset of array `A` to heapify (used in heap
     sort). When defined, array won't be "heapified" below index of `n-1`.
    :return: None. List `A` is mutated.
    """
    if n is None:
        n = len(A)  # Heapify entire array
    l = 2 * i + 1   # Index of a left child
    r = 2 * i + 2   # Index of a right child
    i_largest = i   # Index of a largest element (`i` by default)

    if l < n and A[l] > A[i]:
        i_largest = l
    if r < n and A[r] > A[i_largest]:
        i_largest = r
    if i_largest != i:
        A[i], A[i_largest] = A[i_largest], A[i]
        max_heapify(A, i_largest, n)  # Repeat one level down
    else:
        pass  # No changes


def build_max_heap(A):
    """
    Rearranges list `A` into a representation of a max-heap, in a "bottom-up"
     manner, ensuring that the heap properties are maintained.
    :param A: Array (list) to heapify
    :return: None. List `A` is mutated.
    """

    i_n = len(A) - 1  # Index of a last element
    i_n_2 = i_n // 2  # Index of last element's parent

    for i in range(i_n_2, -1, -1):
        max_heapify(A, i)


def heap_extract_max(A):
    """
    Removes max element from the top of the heap and returns it.
    :param A: Array (list) to heapify
    :return: Max element. List `A` is mutated in the process.
    """
    n = len(A)   # Heap size
    i_n = n - 1  # Index of a last element

    if n < 1:
        raise ValueError("Heap underflow")

    m = A[0]           # Take the top element
    A[0] = A.pop(i_n)  # Move bottom element to the top
    max_heapify(A, 0)  # Fix the heap
    return m
