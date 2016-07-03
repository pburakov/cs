def merge_sort(A):
    """
    Sorts an array of objects using merge-sort algorithm and returns sorted array.

    Merge sort is a recursive sorting algorithm that first recursively splits an array
     in half until it reaches two arrays containing a single element, that are already
     sorted by definition.

    The recursive nature of merge sort is a great example of divide-and-conquer technique,
     when the problem is broken to smaller pieces each of which is trivially solved.
     Solved parts are combined back together.

    Merge operation does the both the "conquer" and "combine" part, merging two sorted
     arrays. The body of the merge-sort method implements the recursive "divide", or
     the slicing of the array.

    Complexity: O(n log(n)) in all cases. `Log(n)` for splitting, `n` for merge. Merge
     sort is stable and it requires additional memory to hold the sliced halves.
    :param list A: Array (list) to sort
    :return list: Sorted product of array `A`
    """
    n = len(A)
    if n < 2:
        return A  # Already sorted by definition
    else:
        i_n_2 = n // 2  # Slice-point
        L = merge_sort(A[:i_n_2])
        R = merge_sort(A[i_n_2:])
        return merge(L, R)


def merge(L, R):
    """
    Merges two sorted arrays into a single array and returns it.

    The algorithm repeatedly looks at elements at the two pointers, picks the one that
     is smaller and adds it to the output. The respective pointer is then shifted one
     position and loop is repeated.

    The merge routine is widely used in other algorithms in various optimized versions.

    Complexity: O(k), where `k` is the sum of the length of two arrays.
    :param list L: Sorted array
    :param list R: Sorted array
    :return list: Merged product of arrays `L` and `R`
    """
    s = len(L) + len(R)  # Final size of the product of the merge
    P = [object] * s  # Allocated memory for the product of the merge
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
