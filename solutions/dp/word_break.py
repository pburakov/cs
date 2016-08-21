"""
Given an input string and a dictionary of words, find out if the input string can be
 segmented into a space-separated sequence of dictionary words. Words can appear more
 than once. Build the resulting sequence.

Example: "amanaplanacanal", dictionary = {"a", "man", "plan", "panama", "canal"}
Output: `['a', 'man', 'a', 'plan', 'a', 'canal']`
"""


def backtrack(S, D, P, i=0):
    """
    Recursive solution to a Word Break problem.

    Recursive approach is straightforward. The string is traversed. If the prefix is
     found in a dictionary, the procedure is repeated for the remainder of the string.

    Complexity: O((n^2)d) on the upper bound, where `n` is the length of a string and `d`
     is the size of a dictionary. Unfortunately, O(n^2) extra space is used for prefix
     storage and memory stack is absorbed on every match.
    :param str S: Input string
    :param set[str] D: Dictionary of words
    :param list P: Output list of words
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
     state. `DP[0..(n-1)]` stores matching prefixes found at `i`-th position.

    Usage of DP allows us to demonstrate an interesting approach to the reconstruction of
     a solution. Here we refer to the DFS algorithm starting at the last matched word, if
     such match has occurred at the left edge, just like in the recursive solution.

    Complexity: O((n^2)d) time, O(nd) space
    :param str S: Input string
    :param set[str] D: Dictionary of words
    :return list: Output list of words
    """
    n = len(S)
    DP = [None] * (n + 1)
    DP[0] = []  # Initial state
    for i in range(0, n):
        if DP[i] is not None:
            for j in range(i + 1, n + 1):
                prefix = S[i:j]
                if prefix in D:
                    if DP[j] is None:
                        DP[j] = []
                    DP[j].append(prefix)
    P = []
    if DP[n] is not None:
        dfs(DP, P, n)
    return P


"""
Auxiliary routines used in the DP solution
"""


def dfs(DP, P, i):
    """
    Subroutine to reconstruct DP solution.

    Complexity: O(w) where `w` is number of matched words.
    :param list DP: List of found and mapped words
    :param P: Output list of words
    :param int i: Starting index (top-down)
    :return None: List `P` is updated
    """
    if DP[i] is not None:
        for word in DP[i]:
            P.insert(0, word)
            dfs(DP, P, i - len(word))
