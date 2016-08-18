def backtrack(S, D, P, i=0):
    """
    :param str S:
    :param set D:
    :param list P:
    :param int i:
    :return bool:
    """
    n = len(S)
    if i == n:
        return True
    else:
        prefix = ''
        for k in range(i, n):
            prefix += S[k]
            if prefix in D and backtrack(S, D, P, k + 1):
                P.insert(0, prefix)
                return True
        return False


def dp(S, D):
    """
    :param str S:
    :param set D:
    :return bool:
    """
    n = len(S)
    if n == 0:
        return True
    DP = [False] * n
    prefix = ''
    for i in range(0, n):
        prefix += S[i]
        if DP[i] is False and prefix in D:
            DP[i] = True
            prefix = ''
        if DP[i] is True:
            suffix = ''
            for k in range(i + 1, n):
                suffix += S[k]
                # Checking if no such prefix was previously found
                if DP[k] is False and suffix in D:
                    DP[k] = True
                    suffix = ''
    # Reconstructing solution
    P = []
    prefix = ''
    if DP[n - 1] is True:
        for i in range(0, n):
            prefix += S[i]
            if DP[i] is True:
                P.append(prefix)
                prefix = ''
    return P
