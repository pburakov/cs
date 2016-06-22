def permutations(L, P, i=0):
    """
    Produces all permutations of a set

    :param list L: Input set
    :param list P: Output list of permutations
    :param int i: Starting index (optional)
    :return None: List `P` is populated
    """
    n = len(L)
    if i == n - 1:
        P.append(L.copy())
        return
    else:
        for k in range(i, n):
            L[i], L[k] = L[k], L[i]
            permutations(L, P, i + 1)
            L[i], L[k] = L[k], L[i]


def subsets(L, P, r=0, w=0, S=None):
    """
    Produces all subsets of a set

    :param list L: Input set
    :param list P: Output list of subsets
    :param int r: Read index (optional) in input set `L`
    :param int w: Write index (optional) in generated subset `S`
    :param list S: Generated subset (optional)
    :return None: List `P` is populated
    """
    n = len(L)
    if S is None:
        S = [None] * n
    if r >= n:
        P.append(S.copy()[0:w])
        return
    else:
        subsets(L, P, r + 1, w, S)
        S[w] = L[r]
        subsets(L, P, r + 1, w + 1, S)
