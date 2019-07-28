"""
Divide and Conquer Sorting Algorithms
=====================================

The recursive nature of merge sort and quicksort are a great example of divide-and-conquer
technique. The problem is broken to smaller pieces, each of which is trivially solved.
Solved parts are joined back together.

Due to the use of divide-and-conquer paradigm, both quicksort and merge sort are well
parallelized.
"""


def quicksort(A, p=0, r=None):
    """Sorts an array in place using quicksort algorithm.

    Quicksort starts with choosing an arbitrary pivot element. Then the array is rearranged
    in such a way, that the elements smaller than the pivot point are on the left side, and
    the elements that are greater than the pivot point are on the right side. After such
    rearrangement, the final position of a pivot element is also its final position in a
    sorted array.

    The left and right sub-arrays are called partitions. They are not immediately sorted.
    The same operation is then ran recursively on both partitions.

    The key to the algorithm is in the partitioning procedure, which can be implemented in
    a variety of ways. In this implementation, partitioning starts with the last item of
    the array. Other implementations use random choice of a pivot point to avoid worst case
    running time on a sorted input.

    Quicksort is unstable. Quicksort parallelizes well thanks to the use of
    divide-and-conquer paradigm.

    Complexity:
        :math:`O(n \log n)`. :math:`O(n^2)` worst case. Quicksort shows good average-case
        efficiency due to a small amount of constant operations in its notation. It does
        not require additional space.

    :param list A: Input array.
    :param int p: Lower bound (default is :math:`0`).
    :param int r: Upper bound (default is :math:`| A | - 1`).

    """
    if r is None:
        r = len(A) - 1
    if p < r:
        q = partition(A, p, r)  # Gets next pivot point
        quicksort(A, p, q - 1)  # Sort left sub-partition
        quicksort(A, q + 1, r)  # Sort right sub-partition


def merge_sort(A):
    """Sorts an array using merge-sort algorithm and returns sorted array.

    Merge sort recursively splits an array in half, until halves a reduced to a single
    element, which effectively makes them sorted by definition. Sorted halves are then
    rearranged back together.

    Merge operation does both the "conquer" and "combine" part as it produces the sorted
    output. The body of the merge-sort method implements the "divide" step, or the
    slicing of the array.

    Merge sort is a stable sorting algorithm.

    Complexity:
        :math:`O(n \log n)` in all cases. :math:`\log n` for splitting, :math:`n` for
        merge. Merge sort requires additional memory to hold the sliced halves.

    :param list A: Array to sort.
    :return: Sorted array.

    """
    n = len(A)
    if n < 2:
        return A  # Already sorted by definition
    else:
        k = n // 2  # Slice-point
        L = merge_sort(A[0:k])
        R = merge_sort(A[k:n])
        return merge(L, R)


"""
Subroutines used in divide-and-conquer sorting
"""


def partition(A, p, r):
    """Partitioning procedure of a quicksort algorithm.

    Partitioning procedure rearranges subarray :math:`A[p..r]` in place. As it runs, the
    array becomes partitioned into four (possibly empty) regions. :math:`A[p..i]`
    contains only the elements that a less than pivot element :math:`x`. :math:`A[i..j]`
    contains only the elements that are greater than :math:`x`. :math:`A[j..r]` are not
    covered by any of these cases. :math:`A[r]` is the pivot element that is placed to its
    final position at index :math:`i`.

    This partitioning scheme is called Lomuto. Partitioning operation has many variations
    (for example, Hoare), and is widely used in other algorithms.

    Complexity:
        :math:`O(k)`, where :math:`k` is the size of a subarray.

    :param list A: Input array.
    :param int p: Lower bound of the partition.
    :param int r: Upper bound of the partition, initial index of pivot element.
    :return: Index of final position of pivot element.

    """
    x = A[r]  # Pivot element
    i = p  # Partitions divider pointer
    for j in range(p, r):
        if A[j] <= x:  # Flip this comparison for reversed order
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[r] = A[r], A[i]  # Transplant pivot element to its final position
    return i


def merge(L, R):
    """Merges two sorted arrays into a single array and returns it.

    The algorithm looks at elements at both sides using two pointers, picks the one that
    is smaller and adds it to the output. The respective pointer is then shifted one
    position and the loop is repeated.

    The merge routine is often found in various algorithms, sometimes in its augmented
    versions. A distributed version of merge routine is called external sort. It operates
    on not just two, but an arbitrary number of arrays.

    Complexity:
        :math:`O(k)`, where :math:`k` is the sum of the length of two arrays.

    :param list L: Sorted array.
    :param list R: Sorted array.
    :return: Merged sorted set from input arrays.

    """
    s = len(L) + len(R)  # Final size of the resulting set
    P = [object] * s  # Allocated memory for the resulting set
    i_l, i_r = 0, 0  # Pointers for arrays `L` and `R`
    max_l, max_r = len(L) - 1, len(R) - 1  # Upper bounds for the pointers
    for i in range(0, s):
        if i_l > max_l:  # Left pointer went out of bounds
            P[i] = R[i_r]
            i_r += 1
            continue  # Skip to the next iteration
        if i_r > max_r:  # Right pointer went out of bounds
            P[i] = L[i_l]
            i_l += 1
            continue  # Skip to the next iteration
        if R[i_r] > L[i_l]:  # Flip this comparison for reversed order
            P[i] = L[i_l]
            i_l += 1
        else:
            P[i] = R[i_r]
            i_r += 1
    return P
