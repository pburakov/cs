def find(T, P):
    """
    Naive string matching algorithm.

    Brute-force search with iteration through string `T`. Least effective when pattern
     `P` contains repeated characters, does increased amount of unnecessary work
     analyzing spurious hits.

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
        if P[0:m] == T[s:s + m]:  # `m` character comparisons
            out.append(s)
    return out
