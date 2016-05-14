def merge_sort(list):
    """
    Merge sort is a recursive sorting algorithm that continuously splits a list in
     half recursively until eventually, it hits two lists containing a single element.
     Sorted halves, starting with two single-element lists (that are already sorted by
     definition) are then merged back together.

    The implementation of merge sort is a great example of divide-and-conquer technique,
     when the problem is broken to smaller pieces each or which is solved and then solved
     parts are combined back together.

    `merge(list)` method does the both the "conquer" and "combine" part, merging two sorted
     arrays. The body of the `merge_sort()` method implements the recursive "divide",
     or the slicing of the array.

    Complexity: O(n log(n)) in all cases. Log(n) for splitting, n for merge.
     Merge Sort requires additional memory to hold the sliced two halves.
    """

    def merge(l, r):
        p = []  # Product of the merge
        ml, mr = len(l), len(r)  # Upper bounds
        il, ir = 0, 0  # Pointers
        while il < ml and ir < mr:
            if r[ir] > l[il]:  # Flip this comparison for reversed ordering
                p.append(l[il])
                il += 1
            else:
                p.append(r[ir])
                ir += 1
        # Unequal lengths of `l` and `r` will result in one of the lists to have remaining
        # items. Adding them using Python's permissive array slicing.
        p.extend(l[il:])
        p.extend(r[ir:])
        return p

    n = len(list)
    n_2 = n // 2
    if n < 2:
        # Base case
        return list
    else:
        # The array will be sliced down recursively to smaller pieces until the base case
        # is hit and then merged back up.
        l = merge_sort(list[0:n_2])
        r = merge_sort(list[n_2:n])
        return merge(l, r)


print(merge_sort([9, 7, 8, 1, 5, 3, 4, 2, 6]))
