"""
Dictionary: {"this", "is", "favorite", "food"}
Source string = "thisismikesfavoritefood"
Output = "this is mikes favorite food"
"""


def solution(S, D):
    _, M = spaces(S, D)
    return reconstruct(S, M)


"""
Auxiliary routines used in the solution
"""


def spaces(S, D, M=None, k=0):
    """
    :param str S:
    :param dict D:
    :param list[bool] M:
    :param int k:
    :return (int, list[bool]):
    """
    n = len(S)
    if M is None:
        M = [False] * n
    if k == n:
        word = ''
        matched = 0
        for i in range(0, n):
            word += S[i]
            if M[i] is True:
                if word in D:
                    matched += len(word)
                word = ''
        return n - matched, M.copy()
    for i in range(k, n):
        M[i] = True
        with_space, map1 = spaces(S, D, M, k + 1)
        M[i] = False
        without_space, map2 = spaces(S, D, M, k + 1)
        if with_space < without_space:
            return with_space, map1
        else:
            return without_space, map2


def reconstruct(S, M):
    """
    :param str S:
    :param list[bool] M:
    :return str:
    """
    out = []
    word = ''
    for i in range(0, len(M)):
        word += S[i]
        if M[i] is True:
            out.append(word)
            word = ''
    return " ".join(out)
