"""
Concentric Print
================

Write a program that will print a concentric rectangular pattern in a two-dimensional
matrix given an input value :math:`n`. The outermost rectangle is formed by :math:`n`,
then the next outermost is formed by :math:`n-1` and so on.

Example::

    Input: n = 3.
    Output:
        3 3 3 3 3
        3 2 2 2 3
        3 2 1 2 3
        3 2 2 2 3
        3 3 3 3 3
"""


def print_concentric(n):
    """Prints concentric two-dimensional pattern.

    The solution uses absolute values to iterate over the range backwards then
    forward.

    Complexity:
        :math:`O(n^2)`, or :math:`\Theta((2n-1)^2)`, which agrees with the size of
        the output, according to the problem statement.

    :param n: Input value.

    """
    for i in range(-n + 1, n):
        for j in range(-n + 1, n):
            print(1 + max(abs(i), abs(j)), end=' ')
        print()
