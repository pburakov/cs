"""
# N Brackets

Write a function that prints all possible combinations of *n* well formed bracket pairs.

This is combinatorial problem whose solution is given by the Catalan numbers, often used
 to demonstrate their recursive formula.
"""


def recursion(o, c=0, S=''):
    """
    Recursive solution for the n bracket pairs problem.

    Recursive formula is straightforward. Every function call will spawn two recursive
     calls, one with added opening bracket, another one with the closing bracket, if
     applicable.

    Complexity: O(2^o), as seen from the recursion tree.
    :param int o: Starting number or number of remaining opening brackets
    :param int c: Number of brackets remaining to be closed (used in recursion)
    :param str S: Intermediate result (used in recursion)
    :return None: Prints to stdout
    """
    if o == c == 0:
        print(S)
        return
    if o > 0:
        recursion(o - 1, c + 1, S + '(')
    if c > 0:
        recursion(o, c - 1, S + ')')
