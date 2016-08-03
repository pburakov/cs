def find(T, P, d=256, q=239):
    """
    Rabin-Karp string matching algorithm.

    This optimized algorithm reduces the amount of spurious hits over the naive approach
     by making use of character-based rolling hash.

    First it calculates the hash of the pattern. As it rolls the search window against
     the string `T`, it copmutes the hash of the characters within that window in an
     effective way. If both hashes match, finally it performs character-to-character
     comparison to rule out false-positives.

    Hash function takes advantage of the observation how characters shift in a rolling
     window. Aside from one character rolling out of focus and one appearing, most of
     the characters within the window remain the same. Hash function of a window can be
     written as:
    ```
    h(w) = -h(cr) + h(c0) + h(c1) ... + h(cm-1) + h(cm)
              ^                                    ^
      removed character                      new character
    ```
    The number of spurious hits is less probable with the better uniform distribution of
     a hash function. Such distribution is achieved with the use of base `d` comparable
     to a cardinality of a character set being used and a large prime number `q`.

    Complexity: O((n - m + 1) m) worst case, however the algorithm performs much better
     on average case (O(n+m)), due to lesser amounts of spurious hits, with correctly
     chosen `d` and `q`.
    :param str T: Target string (haystack)
    :param str P: Pattern string (needle)
    :param int d: Cardinality of a character set (default is 256, corresponding to ASCII)
    :param int q: Prime number (default is 239, closest to the space of 256)
    :return list[int]: List of indices where pattern `P` occurs in a target string
    """
    n = len(T)
    m = len(P)
    h = pow(d, m - 1) % q  # May overflow for large `d`
    p = 0
    t = 0
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
