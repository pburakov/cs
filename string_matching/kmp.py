def find(T, P):
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
            q = π[q - 1]
        if P[q] == T[i]:
            q += 1
        if q == m:
            out.append(i - m + 1)
            q = 0
    return out


def kmp_prefix_function(P):
    """
    Constructs prefix function for use in Knuth-Morris-Pratt algorithm.

    This procedure precomputes a partial match table `π` where `π[q]` is the length of
     the longest prefix of pattern `P` that is a proper suffix of `P[q]`.

    Complexity: O(m) amortized.
    :param str P: Pattern string
    :return list[int]: Prefix table
    """
    m = len(P)
    π = [0] * m  # Partial match table or prefix function
    k = 0
    for q in range(1, m):
        while k > 0 and P[k] != P[q]:
            k = π[k - 1]
        if P[k] == P[q]:
            k += 1
        π[q] = k
    return π
