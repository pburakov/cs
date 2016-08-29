def sort(A, p=0, r=None):
    """
    Sorts an array of objects in place using quicksort algorithm.

    Quicksort, like merge sort, applies the divide-and-conquer paradigm. It chooses an
     arbitrary pivot element. Then the array is rearranged in such a way, that the
     elements smaller than the pivot point are on the left side, and elements that are
     greater than the pivot point are on the right side. After such rearrangement, the
     final position of a pivot element is also its final position in a sorted array.

    These left and right sub-arrays are called partitions. They are not immediately
     sorted, and the same operation is then applied recursively to both partitions.

    The key to the algorithm is in the partitioning procedure, which can be implemented in
     a variety of ways. In this implementation partitioning starts with the last item of
     the array as the initial pivot element. Other implementations use random choice of
     pivot to avoid worst case running time on sorted input.

    Quick sort parallelizes well due to the use of divide-and-conquer method.

    Complexity: O(n log(n)), O(n^2) worst case. Quicksort shows good average-case
     efficiency due to a small amount of constant operations in its notation. Quicksort is
     unstable, however, it does not require additional space.
    :param list A: Input array
    :param int p: Lower bound (default is 0)
    :param int r: Upper bound (default is `|A|-1`)
    :return None:
    """
    if r is None:
        r = len(A) - 1
    if p < r:
        q = partition(A, p, r)  # Gets next pivot point
        sort(A, p, q - 1)  # Sort left sub-partition
        sort(A, q + 1, r)  # Sort right sub-partition


def partition(A, p, r):
    """
    Partitioning procedure of a quicksort algorithm.

    Partitioning procedure rearranges subarray `A[p..r]` in place. As it runs, the array
     becomes partitioned into four (possibly empty) regions. `A[p..i]` contains only
     elements that a less than pivot element `x`. `A[i..j]` contains only elements that
     are greater than `x`. `A[j..r]` are not covered by any of these cases. `A[r]` is the
     pivot element that is placed to its final position at index `i`.

    This partitioning scheme is called Lomuto. Partitioning operation has many variations
     (Hoare, parallellized quicksort and others) and is widely used in other algorithms.

    Complexity: O(k), where `k` is the size of a subarray.
    :param list A: Input array
    :param int p: Lower bound of the partition
    :param int r: Upper bound of the partition, initial index of pivot element
    :return int: Index of final position of pivot element
    """
    x = A[r]  # Pivot element
    i = p  # Partitions divider pointer
    for j in range(p, r):
        if A[j] <= x:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[r] = A[r], A[i]  # Transplant pivot element to its final position
    return i
