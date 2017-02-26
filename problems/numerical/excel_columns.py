"""
Excel column names
==================

Write an algorithm to translate Excel column names to their respective integer serial number.

Examples::

    "A" -> 1
    "Z" -> 26
    "AA" -> 27
    "AABB" -> 18306

"""


def solution(S):
    """Converts Excel's column name to a serial number.

    :param str S: String representation of column.
    :return: Integer serial number of a column.

    """
    n = 0
    i = 0
    for c in S[::-1]:
        n += (ord(c) - ord('A') + 1) * ((ord('Z') - ord('A') + 1) ** i)
        i += 1
    return n
