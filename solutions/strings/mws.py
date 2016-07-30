"""
Your are given a haystack string `S` and a significantly smaller needle string `T`. Find
 a minimum-length substring of `S` that would contain all the characters of a string `T`.
 Duplicates and other elements are allowed.

Example: `S="ADOBECODEBANC", T="ABC". Output: "BANC".
"""


def solution(S, T):
    """
    Minimum window substring solver.

    There is an obvious O((n^2)m) brute-force exhaustive search solution to generate all
     possible sub-strings and then find the shortest one that will contain all the
     characters from string `T`.

    The key observation is that a substring will always begin and end with a character
     that is a member of a set `T`. Optimized algorithm used in this solution runs a
     rolling window, while keeping track of the target characters included in it. At first
     it extends the rihgt edge of the window. As soon as all the target characters are
     seen within the window at least once it starts shrinking the window at left edge
     until one of the elements is no longer in the window. The achieved length of the
     window and indices are saved for further comparison. The extention process is then
     repeated, all wrapped in a `while` loop.

    This solution will work for regular arrays.

    Complexity: O(nm) where `n` is the length of the source string, and `m` is the length
     of the target string.
    :param str S: Haystack string (source)
    :param str T: Needle string (target)
    :return str: A minimum window substring
    """
    n = len(S)
    W = init_freq_map(T)
    l, r = 0, 1
    min_len = inf
    min_l, min_r = 0, 0
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
    """
    Initializes a frequency map (dictionary) from a target string.

    Complexity: O(m) where `m` is the length of a target string.
    :param str T: Target string
    :return dict: Initial frequency map containing with 0 count for each character
    """
    W = {}
    for c in T:
        W[c] = 0
    return W


def has_all(M):
    """
    Helper method frequency map checker.

    Evaluates if a frequency map `M` has every object in it counted at least once.

    Complexity: O(m) where `m` is the number of elements in the map
    :param dict M: Object frequency map
    :return bool: Result of the evaluation
    """
    for c in M:
        if M[c] < 1:
            return False
    return True
