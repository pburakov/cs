def solution(S, D):
    """
    Add spaces problem solver.

    Complexity: O(2^n) without memoization optimization (not implemented)
    :param str S: Input string
    :param set D: Dictionary of words
    :return str: Output string with whitespaces in place
    """
    _, M = spaces(S, D)
    return reconstruct(S, M)


"""
Auxiliary routines used in the solution
"""


def spaces(S, D, M=None, k=0):
    """
    Builds map of whitespace placement with minimum unmatched characters.

    Algorithm exhaustively tries all whitespaces positions and then counts characters of
     the words that matched the dictionary.

    Complexity: O(2^n), can be optimized using memoization (not implemented)
    :param str S: Input string
    :param set D: Dictionary of words
    :param list[bool] M: Intermediate map of whitespaces positions
    :param int k: Rolling index (used in recursion)
    :return (int, list[bool]): Tuple of remaining unmatched characters and
    """
    n = len(S)
    if M is None:  # Initialize intermediate whitespace map
        M = [False] * n
    if k == n:
        word = ''
        matched = 0
        for i in range(0, n):  # Count all characters of matched words
            word += S[i]
            if M[i] is True:
                if word in D:
                    matched += len(word)
                word = ''
        return n - matched, M.copy()
    for i in range(k, n):
        M[i] = True  # Put whitespace
        with_space, map1 = spaces(S, D, M, k + 1)
        M[i] = False  # Remove whitespace
        without_space, map2 = spaces(S, D, M, k + 1)
        if with_space < without_space:
            return with_space, map1
        else:
            return without_space, map2


def reconstruct(S, M):
    """
    Reconstruct solution based on the whitespace map.

    Complexity: O(n)
    :param str S: Input string
    :param list[bool] M: Whitespace map
    :return str: Output string with whitespaces in place
    """
    out = []
    word = ''
    for i in range(0, len(M)):
        word += S[i]
        if M[i] is True:
            out.append(word)
            word = ''
    return " ".join(out)
