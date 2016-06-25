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
        P.append(L.copy())  # Creates an exact copy of L
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
    :param int r: Read index in input set `L` (optional)
    :param int w: Write index in generated subset `S` (optional)
    :param list S: Intermediately generated subset (optional)
    :return None: List `P` is populated
    """
    n = len(L)
    if S is None:
        S = [None] * n
    if r >= n:
        P.append(S[0:w])  # Creates a sliced copy of S
        return
    else:
        subsets(L, P, r + 1, w, S)
        S[w] = L[r]
        subsets(L, P, r + 1, w + 1, S)
