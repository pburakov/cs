def naive(T, P):
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


def kmp(T, P):
    """
    Knuth-Morris-Pratt string matching algorithm.

    Complexity: O(n)
    :param str T: Target string (haystack)
    :param str P: Pattern string (needle)
    :return list[int]: List of indices where pattern `P` occurs in a target string
    """
    n = len(T)
    m = len(P)
    π = kmp_prefix_function(P)
    q = 0
    out = []
    for i in range(0, n):
        while q > 0 and P[q] != T[i]:
            q = π[q]
        if P[q] == T[i]:
            q += 1
        if q == m:
            out.append(i - m + 1)
            q = 0
    return out


def kmp_prefix_function(P):
    """
    Constructs prefix function for use in Knuth-Morris-Pratt algorithm.

    This precomputation procedure computes a partial match table `π` where `π[q]` is the
     length of the longest prefix of pattern `P` that is a proper suffix of `P[q]`.

    Complexity: O(m) amortized.
    :param str P: Pattern string
    :return list[int]: Prefix table
    """
    m = len(P)
    π = [0] * m  # Partial match table or prefix function
    k = 0
    for q in range(1, m):
        while k > 0 and P[k] != P[q]:
            k = π[k]
        if P[k] == P[q]:
            k += 1
        π[q] = k
    return π
