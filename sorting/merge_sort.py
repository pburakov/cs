def merge_sort(list):
    """
    Merge sort is a recursive sorting algorithm that first recursively splits an array
     in half until it reaches two arrays containing a single element (that are already
     sorted by definition). Halves are sorted and merged until an entire array is
     merged back together.

    The recursive nature of merge sort is a great example of divide-and-conquer technique,
     when the problem is broken to smaller pieces each of which is [more or less]
     trivially solved. The solved parts are combined back together.

    `merge(list)` method does the both the "conquer" and "combine" part, merging two sorted
     arrays. The body of the `merge_sort()` method implements the recursive "divide",
     or the slicing of the array.

    Complexity: O(n log(n)) in all cases. Log(n) for splitting, n for merge. Merge sort
     is stable and it requires additional memory to hold the sliced two halves.
    """

    def merge(l, r):
        s = len(l) + len(r)                    # Final size of the product of the merge
        p = [None] * s                         # Allocated memory for the product of the merge
        i_l, i_r = 0, 0                        # Pointers for `l` and `r` arrays
        max_l, max_r = len(l) - 1, len(r) - 1  # Upper bounds for the pointers

        for i in range(0, s):
            # Pointers went out-of-bounds cases (adding element from the remaining side)
            if i_l > max_l:
                p[i] = r[i_r]
                i_r += 1
                continue  # Skip to the next iteration
            if i_r > max_r:
                p[i] = l[i_l]
                i_l += 1
                continue  # Skip to the next iteration
            # Normal in-bound case. Picking smaller element located at the pointer.
            if r[i_r] > l[i_l]:  # Flip this comparison for reversed order
                p[i] = l[i_l]
                i_l += 1
            else:
                p[i] = r[i_r]
                i_r += 1
        return p

    # Body of `merge_sort()`
    n = len(list)

    if n < 2:
        # Base case. Single-element list is already sorted by definition.
        return list
    else:
        # The array will be sliced down recursively to smaller pieces until the base case
        # is hit and then merged back up.
        n_2 = n // 2  # Slice-point
        l = merge_sort(list[0:n_2])
        r = merge_sort(list[n_2:n])
        return merge(l, r)
