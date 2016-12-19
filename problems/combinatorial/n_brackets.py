"""
N Brackets
==========

Write a function that prints all possible combinations of :math:`n` well formed bracket
pairs.

This is combinatorial problem whose solution is given by the Catalan numbers, often used to
demonstrate their recursive formula.
"""


def recursion(n, k=0, S=''):
    """Recursive solution for the n bracket pairs problem.

    Recursive formula is straightforward. Every function call will spawn two recursive
    calls, one with added opening bracket, another one with the closing bracket, if
    applicable.

    Complexity:
        :math:`O(2^n)`, as seen from the recursion tree.

    :param int n: Starting number or number of remaining opening brackets.
    :param int k: Number of brackets remaining to be closed (used in recursion).
    :param str S: Intermediate result (used in recursion).

    """
    if n == k == 0:
        print(S)
        return
    if n > 0:
        recursion(n - 1, k + 1, S + '(')
    if k > 0:
        recursion(n, k - 1, S + ')')
