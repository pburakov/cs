"""
Implement a simple regular expression matcher supporting following expressions:
 - a dot `.` matches a single character
 - a star `*` matches zero or arbitrary repeated characters

Example:
 `R="a*c", S="abc" -> True`
 `R="a.c", S="abbc" -> False`
"""


def match(R, S, i=0, j=0):
    """
    Simple regex recursive problem solver.

    Complexity: O(2^n)
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
