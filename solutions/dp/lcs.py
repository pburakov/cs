def lcs(X, Y, i=None, j=None):
    """
    Returns longest common sub-sequence of two strings calculated recursively.

    This is well known combinatorial problem whose recursive formula is similar to
     a subset algorithm. Recursion compares two elements at given indices, one for
     each string, starting at the end. If matching characters are found, one recursive
     call is made with both indices shifted. Otherwise search continues recursively
     on both strings with one index shifted at a time.

    Complexity: O(2^n) for `m=n`, where `m` and `n` are the lengths of the input
     strings.
    :param str X: First string
    :param str Y: Second string
    :param int i: Lookup index in a first set (used in recursion)
    :param int j: Lookup index in a second set (used in recursion)
    :return str: Output string
    """
    if i is None:
        i = len(X) - 1
    if j is None:
        j = len(Y) - 1
    if i < 0 or j < 0:  # Base case (out of bounds)
        return ''
    elif X[i] == Y[j]:  # Matching characters are found
        return lcs(X, Y, i - 1, j - 1) + X[i]
    else:
        # Recursive calls increasing index for each of the string
        s1 = lcs(X, Y, i, j - 1)
        s2 = lcs(X, Y, i - 1, j)
        # Backtrack with the max. length common string found so far
        if len(s1) > len(s2):
            return s1
        else:
            return s2


def lcs_dp(X, Y):
    """
    Returns longest common sub-sequence of two strings calculated using DP.

    Optimized solution to the same problem using dynamic programming. It almost reads
     like magic, but it should be clear that the underlying logic is the same as the
     recursive approach. Instead of keeping results in the stack, we store calculated
     lengths in the table.

    The key to the solution is backtracking algorithm that reads stored results and
     builds the output based on calculated lengths.

    Complexity: O(mn) or O(n^2) if m=n.
    :param str X: First set
    :param str Y: Second set
    :return str: Output set
    """
    m = len(X)
    n = len(Y)
    DP = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    # Bottom-up saving max length of common sub-sequence at character pairs
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # The logic of populating the table is the same as recursive approach
            if X[i - 1] == Y[j - 1]:
                DP[i][j] = DP[i - 1][j - 1] + 1
            else:
                DP[i][j] = max(DP[i][j - 1], DP[i - 1][j])
    # Backtracking on the results of the calculation
    i, j = m, n  # Vertical and horizontal indices
    k = DP[i][j]  # Start at rightmost bottom cell (max length)
    P = [str] * k  # Allocate memory for the result
    # Start navigating the table
    while i > 0 and j > 0:
        # Characters match: navigating diagonally one cell up-left
        if X[i - 1] == Y[j - 1]:
            P[k - 1] = X[i - 1]
            i -= 1
            j -= 1
            k -= 1
        # No match: navigate towards larger value
        elif DP[i - 1][j] > DP[i][j - 1]:
            i -= 1  # Up (larger value is above)
        else:
            j -= 1  # Left (larger value is in the same row)
    return "".join(P)
