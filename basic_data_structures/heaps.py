"""
Binary heap is a basic implementation of a **priority queue**. Although heap is presented
as a binary tree, is is usually implemented as an array (or a list in Python) because the
tree representation of a heap is nearly complete.

Given that the first index of a tree starts at :math:`0`, the index of a child node in an
array representation can be computed as :math:`2i + 1` for left side child and :math:`2i +
2` for right side child.

Representation invariant of a binary heap determines its main use and common variations:
**max-heap** and **min-heap**. For max-heap, every element is bigger than its children
(vise versa for min heap). Thus, by induction, it can be proven that the largest (or
smallest in case of min-heap) element will always be on the top as long as heap properties
are maintained at any modification made to its structure.

Heap structure is useful when a fast :math:`O(1)` access to the top element is required.
However, the remainder of the array is kept partially unsorted. Heaps are commonly in
various algorithms. This heap implementation contains various additional properties, that
help reducing running times in various cases.
"""


def max_heapify(A, i, n=None):
    """Rearranges elements in array to maintain max-heap properties.

    It implicitly assumes that binary trees rooted at indexes :math:`l` and :math:`r`
    (children of :math:`A[i]`) are max-heaps, but that :math:`A[i]` might violate max-heap
    property of being larger element.

    This algorithm lets the value at :math:`A[i]` "float-down" in the max-heap. As a
    result of this operation, the subtree rooted at index :math:`i` obeys the max-heap
    property.

    Complexity:
        :math:`O(\log n)` due to recurrence, or :math:`O(h)` where :math:`h` is the height
        of the heap.

    :param list A: Array to heapify.
    :param int i: Integer index of an element to float down.
    :param int n: Optional integer length of the subset of an input array (used in heap
     sort). When defined, array won't be "heapified" below index of :math:`n-1`.

    """
    if n is None:
        n = len(A)  # Heapify entire array
    l = 2 * i + 1  # Index of a left child
    r = 2 * i + 2  # Index of a right child
    i_largest = i  # Index of a largest element (`i` by default)
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
    """Rearranges an array into a representation of a max-heap.

    Heap is built in a "bottom-up" manner, starting at second to last level of nodes and
    ensuring that the heap properties are maintained.

    Complexity:
        :math:`O(n \log n)` on upper bound, :math:`O(n)` on tighter asymptotic bound.

    :param list A: Array to heapify

    """

    i_n = len(A) - 1  # Index of a last element
    i_n_p = i_n // 2  # Index of last element's parent
    for i in range(i_n_p, -1, -1):
        max_heapify(A, i)


def max_heap_extract(A, fix=True):
    """Removes max element from the top of the heap and returns it.

    Array is mutated in the process.

    Complexity:
        :math:`O(\log n)` from use of :func:`max_heapify()`.

    :param list A: Array to heapify.
    :param bool fix: Determines if heap-fixing step should be performed immediately after
     extraction (default is :data:`True`). Heap properties will not be guaranteed when
     skipped.
    :return: Pointer to the largest elements in the array.

    """
    n = len(A)  # Heap size
    i_n = n - 1  # Index of a last element
    if n < 1:
        raise ValueError("Heap underflow")
    elif n == 1:
        return A.pop(0)  # Return the only element in the heap
    else:
        m = A[0]  # Take the top element
        A[0] = A.pop(i_n)  # Move bottom element to the top
        if fix is True:
            max_heapify(A, 0)  # Fix the heap
        return m


def max_heap_increase_key(A, i):
    """Causes element in a heap to "bubble up" to its appropriate position.

    It is implicitly assumed that heap properties are not violated through the rest of the
    heap. This method is a "bottom-up" version of max-heapify.

    Complexity:
        :math:`O(h)`, where `h` is the height of the heap or worst case. :math:`O(\log n)`
        when element is percolated from bottom to the root.

    :param list A: Array to heapify.
    :param int i: Integer index of an element to bubble up.

    """
    p = (i - 1) // 2  # Parent's index (valid for both left and right child)
    if p >= 0 and A[i] > A[p]:
        A[p], A[i] = A[i], A[p]  # Exchange child with parent
        max_heap_increase_key(A, p)  # Repeat one level up


def max_heap_insert(A, z):
    """Inserts a new element into the heap.

    Newly added element is forced to bubble-up to it's appropriate position to ensure that
    heap properties are maintained.

    Complexity:
        :math:`O(h)`, where :math:`h` is the height of the heap or worst case, :math:`O(
        \log n)`.

    :param list A: Array to heapify.
    :param object z: A new element.

    """
    A.append(z)  # Add element to the bottom of a heap
    n = len(A)  # Length of a heap
    i_n = n - 1  # Index of last element
    if n > 1:
        max_heap_increase_key(A, i_n)


"""
Mirrored algorithms for min-heap
"""


def min_heapify(A, i, n=None):
    """Rearranges elements in array to maintain max-heap properties.
    """
    if n is None:
        n = len(A)
    l = 2 * i + 1
    r = 2 * i + 2
    i_smallest = i
    if l < n and A[l] < A[i]:
        i_smallest = l
    if r < n and A[r] < A[i_smallest]:
        i_smallest = r
    if i_smallest != i:
        A[i], A[i_smallest] = A[i_smallest], A[i]
        min_heapify(A, i_smallest, n)
    else:
        pass


def build_min_heap(A):
    """Rearranges an array into a representation of a min-heap.
    """
    i_n = len(A) - 1
    i_n_p = i_n // 2
    for i in range(i_n_p, -1, -1):
        min_heapify(A, i)


def min_heap_extract(A, fix=True):
    """Removes min element from the top of the heap and returns it.
    """
    n = len(A)
    i_n = n - 1
    if n < 1:
        raise ValueError("Heap underflow")
    elif n == 1:
        return A.pop(0)
    else:
        m = A[0]
        A[0] = A.pop(i_n)
        if fix is True:
            min_heapify(A, 0)
        return m


def min_heap_increase_key(A, i):
    """Causes element in a heap to "bubble up" to its appropriate position.
    """
    p = (i - 1) // 2
    if p >= 0 and A[i] < A[p]:
        A[p], A[i] = A[i], A[p]
        min_heap_increase_key(A, p)


def min_heap_insert(A, z):
    """Inserts a new element into the heap.
    """
    A.append(z)
    n = len(A)
    i_n = n - 1
    if n > 1:
        min_heap_increase_key(A, i_n)
