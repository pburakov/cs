def three_sum(A):
    """
    Finds integers triplets in an array with the sum of 0.

    This might seem like a trivial problem, but a good approach to iterating the
     array while maintaining three pointers in quadratic time.

    Example: [1, -6, 3, 8, -2, 2] -> (-6, -2, 8)

    Complexity: O(n^2)
    :param list[int] A: Input array
    :return list[tuple]: List of output integer triplets
    """
    n = len(A)
    P = []
    if n < 3:
        return P
    A.sort()  # Any sorting algorithm that runs better than O(n^2)
    for i in range(0, n - 2):
        if i == 0 or A[i] > A[i - 1]:
            j = i + 1
            k = n - 1
            while j < k:
                if A[i] + A[j] + A[k] == 0:
                    P.append((A[i], A[j], A[k]))
                    j += 1
                    k -= 1
                    while j < k and A[j] == A[j - 1]:
                        j += 1
                    while j < k and A[k] == A[k + 1]:
                        k -= 1
                elif A[i] + A[j] + A[k] < 0:
                    j += 1
                else:
                    k -= 1
    return P
