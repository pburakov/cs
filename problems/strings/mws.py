"""
Minimum Window Substring
========================

Your are given a haystack string :math:`S` and a significantly smaller needle string
:math:`T`. Find a minimum-length substring of :math:`S` that would contain all the
characters of a string :math:`T`. Duplicates and other elements are allowed.

Example::

    (S="ADOBECODEBANC", T="ABC") -> "BANC"

"""


def solution(S, T):
    """Minimum window substring solver.

    There is an obvious :math:`O(n^2 m)` brute-force exhaustive search solution to generate
    all possible sub-strings and then find the shortest one that will contain all the
    characters from string :math:`T`.

    The key observation is that a substring will always begin and end with a character that
    is a member of a set :math:`T`. Optimized algorithm used in this solution runs a
    rolling window, while keeping track of the target characters included in it. At first
    it extends the right edge of the window. As soon as all the target characters are seen
    within the window at least once it starts shrinking the window at left edge until one
    of the elements is no longer in the window. The achieved length of the window and
    indices are saved for further comparison. The extension process is then repeated, all
    wrapped in a ``while`` loop.

    This solution will work for regular arrays. It's a great example of "rolling window"
    approach for solving Array and String problems.

    Complexity:
        :math:`O(nm)` where :math:`n` is the length of the source string, and :math:`m` is
        the length of the target string.

    :param str S: Haystack string (source).
    :param str T: Needle string (target).
    :return: A minimum window substring.

    """
    n = len(S)
    W = init_freq_map(T)
    l, r = 0, 1
    min_len = inf
    min_l, min_r = 0, 0
    if S[0] in W:
        W[S[0]] += 1
    while r < n:
        if S[r] in W:
            W[S[r]] += 1
        while has_all(W) and l < r:
            if S[l] in W:
                W[S[l]] -= 1
            if l - r < min_len:
                min_len = r - l
                min_r = r + 1
                min_l = l
            l += 1
        r += 1
    return S[min_l: min_r]


"""
Auxiliary routines and constants used in the solution
"""
inf = float("inf")


def init_freq_map(T):
    """Initializes a frequency map (dictionary) from a target string.

    Complexity:
        :math:`O(m)` where :math:`m` is the length of a target string.

    :param str T: Target string.
    :return: Initial frequency map containing with 0 count for each character.

    """
    W = {}
    for c in T:
        W[c] = 0
    return W


def has_all(M):
    """Helper method frequency map checker.

    Evaluates if a frequency map :math:`M` has every object in it counted at least once.

    Complexity:
        :math:`O(m)` where `m` is the number of elements in the map.

    :param dict M: Object frequency map.
    :return: Boolean result of the evaluation.

    """
    for c in M:
        if M[c] < 1:
            return False
    return True
