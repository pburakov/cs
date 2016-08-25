"""
Given a symbolic boolean expression containing `0`s (False), `1`s (True) and symbols `^` (XOR), `|` (OR) and `&` (AND), count in how many ways it can be parenthesized in order to evaluate to a given value.

Examples:
    `count_ways("1^0|0|1", False) -> 2`
    `count_ways("0&0&0&1^1|0", True) -> 10`

"""


def count_ways(S, b):
    """
    :param str S: Input expression
    :param bool b: Boolean result
    :return int: Number of ways expression `S` can be parenthesized
    """
    n = len(S)
    if n == 0:
        return 0
    if n == 1:
        return int((S == '1') == b)
    ways = 0
    for i in range(1, n, 2):
        c = S[i]
        left = S[0:i]
        right = S[i + 1:n]
        l_true = count_ways(left, True)
        r_true = count_ways(right, True)
        l_false = count_ways(left, False)
        r_false = count_ways(right, False)
        total = (l_true + l_false) * (r_true + r_false)
        total_true = 0
        if c == '^':
            total_true = l_true * r_false + l_false * r_true
        elif c == '&':
            total_true = l_true * r_true
        elif c == '|':
            total_true = l_true * r_true + l_false * r_true + l_true * r_false
        if b is True:
            ways += total_true
        else:
            ways += total - total_true
    return ways
