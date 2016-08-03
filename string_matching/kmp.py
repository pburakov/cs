def find(T, P):
    """
    Knuth-Morris-Pratt string matching algorithm.

    This optimized string matching algorithm is based on idea of string matching
     automata, which examine each text character exatly once. Once a matching character
     is found, the machine transitions to a pattern matching state and remains in such
     while the next character is also accepted.

    When we are in the matching state and a potential pattern match is rejected, but
     another patern occurrence can begin with the previously matched prefix, we can roll
     back our pattern to the last matching character and continue our evaluation, without
     shifting the target string.

    Complexity: O(n) amortized.
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
            q = π[q - 1]  # Next character does not match
        if P[q] == T[i]:
            q += 1  # Next character matches
        if q == m:
            out.append(i - m + 1)
            q = 0  # All of the `P` matched, reset automata
    return out


def kmp_prefix_function(P):
    """
    Constructs prefix function for use in Knuth-Morris-Pratt algorithm.

    This procedure precomputes a partial match table `π`, where `π[q]` is the length of
     the longest prefix of pattern `P` that is a proper suffix of `P[q]`. Note that both
     procedures have much in common, because both match a string against the pattern,
     only prefix function encapsulates knowledge about how the pattern matches against
     itself.

    Example table for `P="ababaca"`: `π=[0, 0, 1, 2, 3, 0, 1]`.

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
