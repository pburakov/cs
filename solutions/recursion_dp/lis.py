"""
Longest increasing subsequence, or LIS, if a sequence of increasing, not necessarily
 continuous elements of an input set in order of their appearance. Single element is LIS
 by definition.

Example: `A=[2, 4, 3, 5, 1, 7, 6, 9, 8, 6]`, `output=[2, 3, 5, 6, 8]`.
"""


def dp(A):
    """
    Returns longest increasing subsequence of a set.

    Let's skip the recursive definition and jump straight to DP. It may seem like there's
     a lot of magic going on, but really, it's all about building the following DP table:
     ```
                Input: 2 4 3 5 1 7 6 9 8 6
     DP[i] (LIS at i): 1 2 2 3 1 4 4 5 5 4   last max DP[i]=5 (i=8)
        Predecessor i: - - 0 2 - - 3 - 6 -   <-- direction of output reconstruction
              Index i: 0 1 2 3 4 5 6 7 8 9
               Output: 2 - 3 5 - - 6 - 8 -
     ```
    Output LIS can be constructed by traversing `DP` table backwards. `DP[i]` is the
     length of the longest subsequence seen so far, if the element `i` was in it.

    Complexity: O(n) and O(n+p) space for DP tables.
    :param list A: Input set (list) of comparable objects
    :return list: Output subsequence
    """
    n = len(A)
    DP = [1] * n
    max_lis = 0  # Length of maximum found LIS overall
    for i in range(1, n):
        for j in range(0, i):
            # Note: comparing `DP[i]` and `DP[j]+1` ensures that we increase the length
            # *only* for the subsequence that would include `DP[i]`.
            if A[i] > A[j] and DP[i] < DP[j] + 1:
                DP[i] = DP[j] + 1
        if DP[i] >= max_lis:
            max_lis = DP[i]
    # Interpreting the results of the calculation
    j = max_lis - 1
    P = [object] * max_lis  # Allocating memory for the output
    for i in range(n - 1, -1, -1):
        if DP[i] == max_lis:
            P[j] = A[i]
            max_lis -= 1
            j -= 1
    return P
