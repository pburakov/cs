"""
Longest Common Substring
========================

Longest Common Substring, Longest Common Subsequence (LCS for short) is similar to many
other dynamic programming puzzles.

Given two strings, :math:`X` and :math:`Y`, find the longest string which is substring of
both :math:`X` and :math:`Y`. The longest common substring of the strings `"BABCA"` and
`"ABCBA"` is the string `"ABC"` of length :math:`3`.
"""


def backtrack(X, Y, i=0, j=0):
    """Returns longest common substring of two strings calculated recursively.

    This is well known combinatorial problem whose recursive formula is similar to a
    subset algorithm. Recursion compares two elements at given indices. If matching
    characters are found, one recursive call is made with both indices shifted. Otherwise
    search continues recursively with one index shifted at a time.

    The solution is based on *Edit Distance* solution routine, but returns an actual string.

    Complexity:
        :math:`O(2^n)` for :math:`m=n`, where :math:`m` and :math:`n` are the lengths of
        the input strings. Tremendous usage of memory stack.

    :param str X: First string.
    :param str Y: Second string.
    :param int i: Lookup index in a first string (used in recursion).
    :param int j: Lookup index in a second string (used in recursion).
    :return: Output string.

    """
    # TODO: Fails on some tests
    if i < len(X) and j < len(Y):
        a, b = X[i], Y[j]
        if a == b:
            return a + backtrack(X, Y, i + 1, j + 1)  # Adding character to a substring
        else:
            # Recursive calls increasing index for each of the string
            s1 = backtrack(X, Y, i, j + 1)
            s2 = backtrack(X, Y, i + 1, j)
            # Backtrack with the max. length common string found so far
            if len(s1) > len(s2):
                return s1
            else:
                return s2
    else:
        return ''  # Base case (out of bounds)


def dp(X, Y):
    """Returns longest common sub-sequence of two strings calculated using DP.

    Optimized solution to the same problem using dynamic programming. It almost reads
     like magic, but it should be clear that the underlying logic is the same as the
     recursive approach. Instead of keeping results in the stack, we store calculated
     lengths in the table `DP`. Note that indexes are shifted to return valid output for
     empty strings.

    The key to the solution is in reconstruction algorithm that reads the computed table
     in sequence and builds the output based on calculated lengths.

    Complexity:
        :math:`O(mn)` or :math:`O(n^2)` if :math:`m=n`. :math:`O(mn)` extra space.

    :param str X: First string.
    :param str Y: Second string.
    :return: Output string.

    """
    m = len(X)
    n = len(Y)
    DP = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # The logic of populating the table is the same as recursive approach
            a, b = X[i - 1], Y[j - 1]
            if a == b:
                DP[i][j] = DP[i - 1][j - 1] + 1
            else:
                DP[i][j] = max(DP[i][j - 1], DP[i - 1][j])
    # Reconstructing solution based on results of the calculation
    i, j = m, n
    k = DP[i][j]  # Start at rightmost bottom cell (max length)
    P = [str] * k  # Allocate memory for the output
    while i > 0 and j > 0:
        # Characters match: navigating diagonally one cell up-left
        a, b = X[i - 1], Y[j - 1]
        if a == b:
            P[k - 1] = a  # Add to output
            i -= 1
            j -= 1
            k -= 1
        # No match: navigate towards larger value
        elif DP[i - 1][j] > DP[i][j - 1]:
            i -= 1  # Up (larger value is above)
        else:
            j -= 1  # Left (larger value is in the same row)
    return "".join(P)


def length(X, Y):
    """Simplified version of LCS algorithm that only returns length.

    Complexity:
        :math:`O(n^2 m)` for :math:`m=n`, where :math:`m` and :math:`n` are the lengths of
        the input strings. Remarkably, it uses :math:`O(1)` space.

    :param str X: First string.
    :param str Y: Second string.
    :return: Length of the longest common substring.

    """
    i, j = 0, 0
    max_len = 0
    n = len(X)
    m = len(Y)
    while i < n:
        j = 0
        while j < m:
            c = 0  # Matching characters counter
            while i + c < n and j + c < m and X[i + c] == Y[j + c]:
                c += 1
            max_len = max(max_len, c)
            j += 1
        i += 1
    return max_len
