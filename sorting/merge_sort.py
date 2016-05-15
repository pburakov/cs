def merge_sort(A):
    """
    Merge sort is a recursive sorting algorithm that first recursively splits an array
     in half until it reaches two arrays containing a single element (that are already
     sorted by definition). Halves are sorted and merged until an entire array is
     merged back together.

    The recursive nature of merge sort is a great example of divide-and-conquer technique,
     when the problem is broken to smaller pieces each of which is [more or less]
     trivially solved. The solved parts are combined back together.

    `merge(A)` method does the both the "conquer" and "combine" part, merging two sorted
     arrays. The body of the `merge_sort()` method implements the recursive "divide",
     or the slicing of the array.

    Complexity: O(n log(n)) in all cases. Log(n) for splitting, n for merge. Merge sort
     is stable and it requires additional memory to hold the sliced two halves.
    """

    def merge(L, R):
        s = len(L) + len(R)                    # Final size of the product of the merge
        P = [None] * s                         # Allocated memory for the product of the merge
        i_l, i_r = 0, 0                        # Pointers for arrays `L` and `R`
        max_l, max_r = len(L) - 1, len(R) - 1  # Upper bounds for the pointers

        for i in range(0, s):
            # Pointers went out-of-bounds cases (adding element from the remaining side)
            if i_l > max_l:
                P[i] = R[i_r]
                i_r += 1
                continue  # Skip to the next iteration
            if i_r > max_r:
                P[i] = L[i_l]
                i_l += 1
                continue  # Skip to the next iteration

            # Normal in-bound case. Picking smaller element located at the pointer.
            if R[i_r] > L[i_l]:  # Flip this comparison for reversed order
                P[i] = L[i_l]
                i_l += 1
            else:
                P[i] = R[i_r]
                i_r += 1
        return P

    # Body of `merge_sort()`
    n = len(A)

    if n < 2:
        # Base case. Single-element list is already sorted by definition.
        return A
    else:
        # The array will be sliced down recursively to smaller pieces until the base case
        # is hit and then merged back up.

        i_n_2 = n // 2  # Slice-point

        L = merge_sort(A[:i_n_2])
        R = merge_sort(A[i_n_2:])
        return merge(L, R)  # Return product of the merge
