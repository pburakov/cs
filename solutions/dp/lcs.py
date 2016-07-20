"""
Longest Common Substring, or LCS, is a very close variation of a Longest Common
 Subsequence and many other dynamic programming puzzles.

Given two strings, `X` and `Y`, find the longest string which is substring of both `X` and
 `Y`. The longest common substring of the strings "ABABC", "BABCA" and "ABCBA" is string
 "ABC" of length 3. Other common substrings are "A", "AB", "B", "BA", "BC" and "C".

Its solution is based on Edit Distance solution routine, but returns an actual string.
"""


def backtrack(X, Y, i=None, j=None):
    """
    Returns longest common substring of two strings calculated recursively.

    This is well known combinatorial problem whose recursive formula is similar to a
     subset algorithm. Recursion compares two elements at given indices, one for each
     string, starting at the end. If matching characters are found, one recursive call
     is made with both indices shifted. Otherwise search continues recursively on both
     strings with one index shifted at a time.

    Complexity: O(2^n) for `m=n`, where `m` and `n` are the lengths of the input strings.
    :param str X: First string
    :param str Y: Second string
    :param int i: Lookup index in a first string (used in recursion)
    :param int j: Lookup index in a second string (used in recursion)
    :return str: Output string
    """
    if i is None:
        i = len(X) - 1
    if j is None:
        j = len(Y) - 1
    if i < 0 or j < 0:  # Base case (out of bounds)
        return ''
    a, b = X[i], Y[j]
    if a == b:
        return backtrack(X, Y, i - 1, j - 1) + a  # Adding character to a substring
    else:
        # Recursive calls increasing index for each of the string
        s1 = backtrack(X, Y, i, j - 1)
        s2 = backtrack(X, Y, i - 1, j)
        # Backtrack with the max. length common string found so far
        if len(s1) > len(s2):
            return s1
        else:
            return s2


def dp(X, Y):
    """
    Returns longest common sub-sequence of two strings calculated using DP.

    Optimized solution to the same problem using dynamic programming. It almost reads like
     magic, but it should be clear that the underlying logic is the same as the recursive
     approach. Instead of keeping results in the stack, we store calculated lengths in
     the table `DP`. Note that indexes are shifted to return valid output for empty strings.

    The key to the solution is in reconstruction algorithm that reads the computed table
     in sequence and builds the output based on calculated lengths.

    Complexity: O(mn) or O(n^2) if m=n.
    :param str X: First string
    :param str Y: Second string
    :return str: Output string
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
