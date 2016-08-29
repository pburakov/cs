"""
Binary Heap is a basic implementation of a Priority Queue. Although heap is presented
 as a Binary Tree, is is usually implemented as an array (or a list in Python)
 because the tree representation of a heap is nearly complete.

Given that the first index of a tree starts at `0`, the index of a child node in an
 array representation can be computed as `i * 2 + 1` for left side child and
 `i * 2 + 2` for right side child.

Representation invariant of a Binary Heap determines its main use and common
 variations: max-heap and min-heap. For max-heap, every element is bigger than
 its children. Thus, by induction, it can be proven that the largest element will
 always be on the top as long as heap properties are maintained at any modification
 made to its structure.

Heap structure is useful when a fast O(n) access to the top element is required,
 however, the remainder of the array is kept partially unsorted. Heaps are commonly
 in various algorithms. This heap implementation contains various additional
 arguments, that helps reducing running times in various cases.
"""


def max_heapify(A, i, n=None):
    """
    Rearranges array `A` "below" index `i` to maintain max-heap properties.

    It implicitly assumes that binary trees rooted at indexes `l` and `r` (children of
     `A[i]`) are max-heaps, but that A[i] might violate max-heap property of being
     larger element.

    This algorithm lets the value at `A[i]` "float-down" in the max-heap so that the
     subtree rooted at index `i` obeys the max-heap property.

    Complexity: O(log(n)) due to recurrence, or O(h) where `h` is the height of the heap.
    :param list A: Array (list) to heapify
    :param int i: Integer index of an element to float down
    :param int n: Optional integer length of the subset of array `A` to heapify (used
     in heap sort). When defined, array won't be "heapified" below index of `n-1`.
    :return None: List `A` is mutated.
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
    Rearranges list `A` into a representation of a max-heap.

    Heap is built in a "bottom-up" manner, starting at second to last level of nodes
     and ensuring that the heap properties are maintained.

    Complexity: O(n log(n)) on upper bound, O(n) on tighter asymptotic bound.
    :param list A: Array (list) to heapify
    :return None: List `A` is mutated.
    """

    i_n = len(A) - 1  # Index of a last element
    i_n_p = i_n // 2  # Index of last element's parent
    for i in range(i_n_p, -1, -1):
        max_heapify(A, i)


def heap_extract_max(A, fix=True):
    """
    Removes max element from the top of the heap and returns it.

    Complexity: O(log(n)) from use of `max_heapify()`
    :param A: Array (list) to heapify
    :param bool fix: Determines if heap-fixing step should be performed immediately
     after extraction (default is True). Heap properties will not be guaranteed
     when skipped.
    :return Any: Largest element, or a pointer to the largest elements of list `A`.
     List `A` is mutated in the process.
    """
    n = len(A)   # Heap size
    i_n = n - 1  # Index of a last element
    if n < 1:
        raise ValueError("Heap underflow")
    elif n == 1:
        return A.pop(0)    # Return the only element in the heap
    else:
        m = A[0]           # Take the top element
        A[0] = A.pop(i_n)  # Move bottom element to the top
        if fix is True:
            max_heapify(A, 0)  # Fix the heap
        return m


def heap_increase_key(A, i):
    """
    Causes i-th element in a heap to "bubble up" to its appropriate position.

    It is implicitly assumed that heap properties are not violated through the rest of
     the heap. This method is a "bottom-up" version of max-heapify.

    Complexity: O(h), where `h` is the height of the heap or worst case. O(log(n))
     when element is percolated from bottom to the root.
    :param list A: Array (list) to heapify
    :param int i: Integer index of an element to bubble up
    :return None: List `A` is mutated.
    """
    p = (i - 1) // 2  # Parent's index (valid for both left and right child)
    if p >= 0 and A[i] > A[p]:
        A[p], A[i] = A[i], A[p]  # Exchange child with parent
        heap_increase_key(A, p)  # Repeat one level up


def max_heap_insert(A, z):
    """
    Inserts a new element into the heap.

    Newly added element is forced to bubble-up to it's appropriate position to ensure
     that heap properties are maintained.

    Complexity: O(h), where `h` is the height of the heap or worst case, O(log(n))
    :param list A: Array (list) to heapify
    :param object z: Pointer or an instance of a new element
    :return None: List `A` is mutated.
    """
    A.append(z)  # Add element to the bottom of a heap
    n = len(A)   # Length of a heap
    i_n = n - 1  # Index of last element
    if n > 1:
        heap_increase_key(A, i_n)
