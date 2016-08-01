def naive(T, P):
    """
    Returns index of first occurrence of a matching pattern string with target string.

    Complexity: O((n-m+1)m). `n-m+1` for the main loop and `m` for every character copmarison
     within a pattern.
    :param str T: Target string (haystack)
    :param str P: Pattern (needle)
    :return int: Index of first occurrence of a matching pattern substring `P` in `T`.
    """
    n = len(T)
    m = len(P)
    for s in range(0, n - m + 1):
        if P[0:m] == T[s:s + m]:
            return s
    return -1


print(naive("abczzz", "abc"))
