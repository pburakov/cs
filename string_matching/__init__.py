"""
String Matching Algorithms
==========================
"""


def naive(T, P):
    """Naive string matching algorithm.

    Brute-force search with iteration through string :math:`T`. Least effective when
    pattern :math:`P` contains repeated characters. This algorithm does unnecessary work
    analyzing spurious hits.

    Complexity:
        :math:`O(m (n - m + 1))`. :math:`n - m + 1` for the main loop and :math:`m` for
        every character comparison within a pattern.

    :param str T: Target string (haystack).
    :param str P: Pattern string (needle).
    :return: List of indices where pattern `P` occurs in a target string.

    """
    n = len(T)
    m = len(P)
    out = []
    for s in range(0, n - m + 1):
        if P[0:m] == T[s:s + m]:  # `m` character comparisons
            out.append(s)
    return out


def rabin_karp(T, P, d=256, q=293):
    """Rabin-Karp "rolling hash" string matching algorithm.

    This optimized algorithm reduces the amount of spurious hits seen in the naive
    approach by using character-based rolling hash.

    First it calculates the hash of the pattern, and it remains constant. As it rolls the
    search window against the string :math:`T`, it computes the hash of all the characters
    occurring within that window in an effective way. If both hashes match, it performs a
    final character-to-character comparison to rule out false-positives.

    Hash function takes advantage of the observation how the characters shift in a rolling
    window. Aside from one character rolling out of the focus and one appearing, other
    characters within the window remain the same. Hash function of a window can be
    written as:

    .. math::
        h(w) = -h(c_r) + h(c_0) + h(c_1) + ... + h(c_{m-1}) + h(c_m)

    Where :math:`h` is a hash function, :math:`c_r` is the removed character, :math:`c_m`
    is a next character "rolled" into a hash window.

    The number of spurious hits is less probable with better uniform distribution of a
    hash function. Such distribution is achieved with the use of base :math:`d` comparable
    to a cardinality of a character set being used, and a large prime number :math:`q`.

    Complexity:
        :math:`O(m (n - m + 1))` worst case, however the algorithm performs much better on
        average case :math:`(O(n+m))`, due to lesser amounts of spurious hits, with
        correctly chosen :math:`d` and :math:`q`.

    :param str T: Target string (haystack).
    :param str P: Pattern string (needle).
    :param int d: Cardinality of a character set (default is 256, corresponding to ASCII).
    :param int q: Prime number (default is 293, closest to the space of 256).
    :return: List of indices where pattern `P` occurs in a target string.

    """
    n = len(T)
    m = len(P)
    h = pow(d, m - 1) % q  # May overflow for large `d`
    p = 0  # Hash of a pattern
    t = 0  # Hash of a window in a target string
    out = []
    for i in range(0, m):  # Preprocessing
        p = (d * p + ord(P[i])) % q
        t = (d * t + ord(T[i])) % q
    for s in range(0, n - m + 1):
        if p == t:  # Candidate is found
            if P[0:m] == T[s:s + m]:
                out.append(s)
        if s < n - m:
            # Hash with character at index `s` removed and character at `s+m` added
            t = (d * (t - ord(T[s]) * h) + ord(T[s + m])) % q
    return out


def kmp(T, P):
    """Knuth-Morris-Pratt string matching algorithm.

    This optimized string matching algorithm is based on a string matching automata which
    examines each text character exactly once. Once a matching character is found,
    the machine transitions to a pattern matching state and remains in such while the next
    consequent character is also accepted.

    When we are in the matching state and a potential pattern match is rejected, another
    pattern occurrence can begin with the previously matched prefix. We can roll back our
    pattern to the last matching character and continue our evaluation, without shifting
    the target string.

    Complexity:
        :math: `O(n)` amortized.

    :param str T: Target string (haystack).
    :param str P: Pattern string (needle).
    :return: List of indices where pattern occurs in a target string.

    """
    n = len(T)
    m = len(P)
    p = kmp_prefix_function(P)
    q = 0
    out = []
    for i in range(0, n):
        while q > 0 and P[q] != T[i]:
            q = p[q - 1]  # Next character does not match
        if P[q] == T[i]:
            q += 1  # Next character matches
        if q == m:
            out.append(i - m + 1)
            q = 0  # All of the `P` matched, reset automata
    return out


"""
Subroutine used in Knuth-Morris-Pratt algorithm.
"""


def kmp_prefix_function(P):
    """Constructs prefix function for use in Knuth-Morris-Pratt algorithm.

    This procedure computes a partial match table :math:`\pi`, where :math:`\pi[q]` is
    the length of the longest prefix of pattern :math:`P` that is a proper suffix of
    :math:`P[q]`. Note how both :data:`kmp()` and :data:`kmp_prefix_function()` have much
    in common, because both match a string against the pattern, only the prefix function
    encapsulates knowledge about how the pattern matches against itself.

    Example table for ``P="ababaca"``: ``p=[0, 0, 1, 2, 3, 0, 1]``.

    Complexity:
        :math:`O(m)` amortized.

    :param str P: Pattern string.
    :return: Prefix table.

    """
    m = len(P)
    p = [0] * m  # Partial match table or prefix function
    k = 0
    for q in range(1, m):
        while k > 0 and P[k] != P[q]:
            k = p[k - 1]
        if P[k] == P[q]:
            k += 1
        p[q] = k
    return p
