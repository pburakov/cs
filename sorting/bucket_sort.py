def bucket_sort(A):
    """
    Sorts an array of integers using bucket sort algorithm and returns sorted array.

    Bucket sort is fast because it makes certain assumptions about the input. It is
     efficient when input is drawn from a uniform distribution. Evenly distributed
     items can be sorted into individual buckets and then drawn back in order.
     Depending on the nature of the input additional sorting routines may be
     performed on each bucket.

    Implementation of bucket sort largely depends on the input data. This variant
     assumes that, for `n`-sized array `A`, items are uniformly distributed integers
     across an interval {0..n}. In order to maintain stability of the sort, buckets
     are represented by dynamic LIFO structures or stacks.

    Complexity: O(n) in average case for uniformly or evenly distributed input
    :param list[int] A: Input array
    :return list[int]: Sorted array
    """
    n = len(A)
    P = [int] * n   # Allocated memory for the sorted output
    B = [None] * n  # Array of buckets
    for i in A:
        if B[i] is None:
            B[i] = []
        B[i].append(i)
    i = n - 1
    for j in range(n - 1, -1, -1):  # Going backwards to maintain stability
        while B[j]:
            P[i] = B[j].pop()
            i -= 1
    return P
