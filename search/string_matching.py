def naive(T, P):
    """
    Naive string matching algorithm.

    Returns index of first occurrence of a matching pattern string with target string.

    Complexity: O((n - m + 1) m). `n - m + 1` for the main loop and `m` for every
     character comparison within a pattern.
    :param str T: Target string (haystack)
    :param str P: Pattern string (needle)
    :return int: Index of first occurrence of a matching pattern substring `P` in `T`.
    """
    n = len(T)
    m = len(P)
    for s in range(0, n - m + 1):
        if P[0:m] == T[s:s + m]:
            return s
    return -1


def rabin_karp(T, P, d=256, q=239):
    """
    Rabin-Karp string matching algorithm.

    Returns index of first occurrence of a matching pattern string with target string.

    Complexity: O((n - m + 1) m), however the algorithm perform much better on average
     case, due to lesser amounts of spurious hits, with correctly chosen `d` and `q`.
    :param str T: Target string (haystack)
    :param str P: Pattern string (needle)
    :param int d: Cardinality of a character set (default is 256, corresponding to ASCII)
    :param int q: Prime number (default is 239, closest to the space of 256)
    :return:
    """
    n = len(T)
    m = len(P)
    h = pow(d, m - 1) % q
    p = 0
    t = 0
    for i in range(0, m):  # Preprocessing
        p = (d * p + ord(P[i])) % q
        t = (d * t + ord(T[i])) % q
    for s in range(0, n - m + 1):
        if p == t:
            if P[0:m] == T[s:s + m]:
                return s
        if s < n - m:
            # Hash with character at index `s` removed and character at `s+m` added
            t = (d * (t - ord(T[s]) * h) + ord(T[s + m])) % q
    return -1


print(rabin_karp("kbazpgabz", "gab"))
