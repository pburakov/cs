"""
Simple Regex Matcher
====================

You are given a source string :math:`S` and a regular expression string :math:`R`.
Implement a simple regular expression matcher supporting following syntax:

    - a dot ``.`` matches a single character;
    - a star ``*`` matches zero or arbitrary repeated characters.

Examples::

    (R="a*c", S="abc") -> True
    (R="a.c", S="abbc") -> False

"""


def match(R, S, i=0, j=0):
    """Simple regex recursive problem solver.

    Complexity:
        :math:`O(n)` where :math:`n` is length of the string.

    :param str R: Regex expression.
    :param str S: Source string.
    :param int i: Index in regex expression (used in recursion).
    :param int j: Index in source string (used in recursion).
    :return: :data:`True` if expression has matched, :data:`False` otherwise.

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
