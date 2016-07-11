def lis(A):
    """
    Longest increasing subsequence of a set.

    Longest increasing subsequence, or LIS, if a sequence of increasing, not necessarily
     continuous elements of an input set in order of their appearance. Single element is
     LIS by definition.

    Example: `A=[2, 4, 3, 5, 1, 7, 6, 9, 8, 6]`, `output=[2, 3, 5, 6, 8]`.

    Let's jump straight to DP rather than maintaining the state of a recursive algorithm.
     It may seem like there's a lot of magic going on, but really, it's all about building
     the following DP table:
     ```
                  Index i: 0 1 2 3 4 5 6 7 8 9
                    Input: 2 4 3 5 1 7 6 9 8 6
         DP[i] (LIS at i): 1 2 2 3 1 4 4 5 5 4   last max DP[i]=5 (i=8)
     Output predecessor i: - - 0 2 - - 3 - 6 -   <-- direction of traversal
     ```
    Output LIS can be constructed by traversing `DP` table backwards.

    Complexity: O(n) and O(n+p) space for DP tables.
    :param list A: Input set (list) of comparable objects
    :return list: Output subsequence
    """
    n = len(A)
    DP = [1] * n  # `DP[i]` is the longest subsequence seen so far at element `i`.
    max_lis = 0  # Length of maximum found found LIS
    for i in range(1, n):
        for j in range(0, i):
            # Comparing `DP[i]` and `DP[j]+1` ensures that we increase the length _only_
            # for the subsequence that would include `DP[i]`.
            if A[i] > A[j] and DP[i] < DP[j] + 1:
                DP[i] = DP[j] + 1
        if DP[i] >= max_lis:  # Keeping track of last seen maximum LIS
            max_lis = DP[i]
    # Backtracking on the results of the calculation
    P = [object] * max_lis  # Allocating memory for the output
    j = max_lis - 1  # Index in output list
    for i in range(n - 1, -1, -1):
        if DP[i] == max_lis:
            P[j] = A[i]
            max_lis -= 1
            j -= 1
    return P
