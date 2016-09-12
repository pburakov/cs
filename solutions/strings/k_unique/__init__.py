def recursive(S, k):
    """
    Length of a substring with at most k unique characters using recursion.

    :param str S: Source string
    :param int k: Number of distinct characters
    :return int: Length of a substring of `S` with at most `k` unique characters
    """
    n = len(S)
    freq_map = {}
    for i in range(0, n):
        freq_map[S[i]] = True
        if len(freq_map) > k:
            return max(i, recursive(S[1:n], k))
    if len(freq_map) <= k:
        return n
    else:
        return 0
