def lis(A):
    """
    Longest increasing subsequence of a set.

    Longest increasing subsequence, or LIS, if a sequence of increasing, not necessarily
     continuous elements of an input set in order of their appearance. Single element is
     LIS by definition.

    Example: `A=[2, 4, 3, 5, 1, 7, 6, 9, 8]`, `output=[2, 3, 5, 6, 8]`.

    Let's jump straight to DP rather than maintaining the state of a recursive algorithm.
     It may seem like there's a lot of magic going on, but really, it's all about building
     this table:
     ```
             Index i: 0 1 2 3 4 5 6 7 8 9
               Input: 2 4 3 5 1 7 6 9 8 3
     L[i] (LIS at i): 1 2 2 3 1 4 4 5 5 2
     ```
    Output LIS can be constructed by traversing this DP table backwards.

    Complexity: O(n) and O(n+p) space for DP tables.
    :param list A: Input set (list) of comparable objects
    :return list: Output subsequence
    """
    n = len(A)
    L = [1] * n  # `L[i]` is the longest subsequence seen so far at element `i`.
    max_lis = 0  # Length of maximum found found LIS
    for i in range(1, n):
        for j in range(0, i):
            if A[i] > A[j] and L[i] < L[j] + 1:
                L[i] = L[j] + 1
        if L[i] >= max_lis:
            max_lis = L[i]
    # Backtracking on the results of the calculation
    P = [object] * max_lis  # Allocating memory for the output
    j = max_lis - 1  # Index in output list
    for i in range(n - 1, -1, -1):
        if L[i] == max_lis:
            P[j] = A[i]
            max_lis -= 1
            j -= 1
    return P


a1 = [2, 4, 3, 5, 1, 7, 6, 9, 8, 3]
print(a1)
print(lis(a1))
