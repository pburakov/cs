def find(T, P, d=256, q=239):
    """
    Rabin-Karp string matching algorithm.

    Returns index of first occurrence of a matching pattern string with target string.

    Complexity: O((n - m + 1) m), however the algorithm perform much better on average
     case, due to lesser amounts of spurious hits, with correctly chosen `d` and `q`.
    :param str T: Target string (haystack)
    :param str P: Pattern string (needle)
    :param int d: Cardinality of a character set (default is 256, corresponding to ASCII)
    :param int q: Prime number (default is 239, closest to the space of 256)
    :return list[int]: List of indices where pattern `P` occurs in a target string
    """
    n = len(T)
    m = len(P)
    h = pow(d, m - 1) % q
    p = 0
    t = 0
    out = []
    for i in range(0, m):  # Preprocessing
        p = (d * p + ord(P[i])) % q
        t = (d * t + ord(T[i])) % q
    for s in range(0, n - m + 1):
        if p == t:
            if P[0:m] == T[s:s + m]:
                out.append(s)
        if s < n - m:
            # Hash with character at index `s` removed and character at `s+m` added
            t = (d * (t - ord(T[s]) * h) + ord(T[s + m])) % q
    return out
