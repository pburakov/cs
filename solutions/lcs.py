def lcs(X, Y, i=None, j=None):
    """
    Returns longest common sub-sequence of two sets found recursively

    This is well known combinatorial problem whose recursive formula is similar to
     a subset algorithm. Recursion compares two elements at given indices, one for
     each string, starting at the end. If matching characters are found, one recursive
     call is made with both indices shifted. Otherwise search continues recursively
     on both strings with one index shifted at a time.

    Related sections: Combinatorial Search, Recursion.

    Complexity: O(2^n) for `m=n`, where `m` and `n` are the lengths of the input
     strings.
    :param list X: First set
    :param list Y: Second set
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
        # Backtrack with the longest string found so far
        if len(s1) > len(s2):
            return s1
        else:
            return s2
