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


def excel(S):
    """Returns the serial number of Excel's column name.

    The algorithm iterates backwards over the input string and adds the exponent of the
    character's ordinal number in the string to the total.

    Complexity:
        :math:`O(k)` where :math:`k` is the number of characters in the string.

    :param str S: String representation of column.
    :return: Integer serial number of a column.

    """
    n = 0
    k = 0
    for c in S[::-1]:  # Iterate backwards
        a = ord(c.capitalize()) - ord('A') + 1  # Character ordinal number in the alphabet
        n += a * 26 ** k
        k += 1
    return n
