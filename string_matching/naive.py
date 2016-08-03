def find(T, P):
    """
    Naive string matching algorithm.

    Returns index of first occurrence of a matching pattern string with target string.

    Complexity: O((n - m + 1) m). `n - m + 1` for the main loop and `m` for every
     character comparison within a pattern.
    :param str T: Target string (haystack)
    :param str P: Pattern string (needle)
    :return list[int]: List of indices where pattern `P` occurs in a target string
    """
    n = len(T)
    m = len(P)
    out = []
    for s in range(0, n - m + 1):
        if P[0:m] == T[s:s + m]:
            out.append(s)
    return out
