"""
Given an input string and a dictionary of words, find out if the input string can be
 segmented into a space-separated sequence of dictionary words. Words can appear more
 than once. Build the resulting sequence.

Example: "amanaplanacanal", dictionary = {"a", "man", "plan", "canal"}
Output: `['a', 'man', 'a', 'plan', 'a', 'canal']`
"""


def backtrack(S, D, P, i=0):
    """
    Recursive solution to a Word Break problem.

    Recursive approach is straightforward. The string is traversed. If the prefix is
     found in a dictionary, the procedure is repeated for the remainder of the string.

    Complexity: O(nd) on the upper bound, where `n` is the length of a string and `d` is
     the size of a dictionary. Complexity would be O(n^3) is we used substrings.
     Unfortunately, O(n!) extra space is used for prefix storage.
    :param str S: Input string
    :param set[str] D: Dictionary of words
    :param list P: Output list
    :param int i: Starting index (used in recursion)
    :return bool: Returns True if the whole string has been matched.
    """
    n = len(S)
    if i == n:
        return True
    else:
        prefix = ''
        for k in range(i, n):
            prefix += S[k]
            if prefix in D and backtrack(S, D, P, k + 1):
                P.insert(0, prefix)
                return True
        return False


def dp(S, D):
    """
    Word Break solution using dynamic programming.

    The DP approach is based on the recursive formula, but uses a table to store the
     state. `DP[0..(n-1)]` stores boolean values indicating if a prefix has been found at
     `i`-th position. This denotes that the string can be broken at this index, which is
     how the solution is constructed.

    Complexity: O(n^2d) and O(n) storage.
    :param str S: Input string
    :param set[str] D: Dictionary of words
    :return list: Output list
    """
    n = len(S)
    if n == 0:
        return []
    DP = [False] * n
    prefix = ''
    for i in range(0, n):
        prefix += S[i]
        # Skipping dictionary lookup if the prefix was already found
        if DP[i] is False and prefix in D:
            DP[i] = True
            prefix = ''
        if DP[i] is True:
            suffix = ''
            for k in range(i + 1, n):
                suffix += S[k]
                # Skipping dictionary lookup if the prefix was already found
                if DP[k] is False and suffix in D:
                    DP[k] = True
                    suffix = ''
    # Reconstructing solution
    P = []
    prefix = ''
    if DP[n - 1] is True:  # Successfully matched the whole string
        for i in range(0, n):
            prefix += S[i]
            if DP[i] is True:
                P.append(prefix)
                prefix = ''
    return P
