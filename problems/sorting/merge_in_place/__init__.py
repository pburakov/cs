def sort(A, B):
    """
    Merge routine for the solution.

    :param list A: First array
    :param list B: Second array of length 2*|A|, second half filled with `0`s
    :return list None: Sorted product goes into array `B` (in place sorting)
    """
    n = len(A)
    a = n - 1  # pointer in array A
    b = n - 1  # pointer to meaningful numbers in array B
    for i in range(2 * n - 1, -1, -1):
        # pointers went out of bounds cases
        if a < 0:
            B[i] = B[b]
            b -= 1
            continue
        if b < 0:
            B[i] = A[a]
            a -= 1
            continue
        # pointers are within bounds
        if A[a] > B[b]:
            B[i] = A[a]
            a -= 1
        else:
            B[i] = B[b]
            b -= 1
