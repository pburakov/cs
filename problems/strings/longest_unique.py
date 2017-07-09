"""
Longest Substring Without Repeating Characters
==============================================

Given a string :math:`S`, find the length of the longest substring without repeating
characters.

Examples::

    "abcabcbb" -> 3 ("abc")
    "bbbbb" -> 1 ("b")
    "pwwkew" -> 3 ("wke")
    "tmmzuxt" -> 5 ("mzuxt")

"""


def solution(S):
    """Returns the length of the longest substring with unique characters.

    There is a brute-force solution which would exhaustively search unique characters
    within all possible substrings, which can yield decent results with memoization.
    However we don't need to repeatedly scan substrings which were already checked to have
    no duplicate characters.

    This more optimal algorithm uses rolling window technique. Right pointer of a window
    scans through the string and stores the index of every character it encounters into the
    table unless a previously seen character is encountered. When this happens left pointer
    is shifted to position immediately after the last seen position of the repeating
    character. Both pointers move only forward.

    Complexity:
        :math:`O(n)` running time and :math:`O(k)` space where :math:`k` is the constant
        number of letters in the alphabet.

    :param str S: Input string.
    :return: Length of the longest substring without repeating characters.

    """
    M = {}  # Map of seen characters and their last known index
    i = 0  # Left pointer
    max_len = 0
    for k in range(len(S)):  # Right pointer
        c = S[k]
        if c in M and M[c] >= i:  # Avoid accidentally jumping back
            i = M[c] + 1  # Shift left pointer one step
        else:
            max_len = max(max_len, k + 1 - i)
        M[c] = k
    return max_len
