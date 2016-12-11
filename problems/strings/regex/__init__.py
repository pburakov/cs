def match(R, S, i=0, j=0):
    """
    Simple regex recursive problem solver.

    Complexity: O(n) where `n` is length of the string.
    :param str R: Regex expression
    :param str S: Source string
    :param int i: Index in regex expression (used in recursion)
    :param int j: Index in source string (used in recursion)
    :return bool: Returns True if expression has matched, False otherwise
    """
    if j == len(S):
        return True
    else:
        if R[i] == '.' or R[i] == S[j]:
            return match(R, S, i + 1, j + 1)
        elif R[i] == '*':
            return match(R, S, i, j + 1)
        else:
            return False
