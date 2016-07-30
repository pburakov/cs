"""
Your are given a haystack string `S` and a significantly smaller needle string `T`.
 Find a minimum-length substring of `S` that would contain all the characters of a
 string `T`. Duplicates and other elements are allowed.

Example: `S="ADOBECODEBANC", T="ABC". Output: "BANC".
"""


def solution(S, T):
    """
    Minimum window substring solver.

    This solution will work for regular arrays.

    :param str S: Haystack string
    :param str T: Needle string
    :return str:
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
    :param str T:
    :return dict:
    """
    W = {}
    for c in T:
        W[c] = 0
    return W


def has_all(W):
    """
    :param dict W:
    :return bool:
    """
    for c in W:
        if W[c] < 1:
            return False
    return True
