"""
Simple Regex Matcher
====================

You are given a source string :math:`S` and a regular expression string :math:`P`.
Implement a simple regular expression matcher supporting the following syntax:

    - a dot ``.`` matches a single character;
    - a star ``*`` matches zero or more of the preceding element.

Examples::

    (S="ab", P="ac") -> False
    (S="a.c", P="abc") -> True
    (S="abbbc", P="ab*c") -> True
    (S="aab", P="c*a*b") -> True

There are multiple variations of this problem of varying complexity. I discuss perhaps
one of the most complex modifications of the problem I've encountered.

The problem is discussed in details here:
https://leetcode.com/articles/regular-expression-matching/

"""
from combinatorial.optimization import memoize


@memoize
def match(S, P, i=0, j=0):
    """Evaluates a source string against a regular expression.

    The complexity rises dramatically with the use of a Kleene star ``"*"``. On every
    star character we need to spawn two recursive branches: one for zero matching
    characters, one for more.

    The use of a lookahead backtracking technique in this algorithms is well suited for
    solving the complexity of the Kleene star and many edge cases it imposes.

    Complexity:
        :math:`O((m+n)2^{m+n})`, optimized to :math:`O(mn)` with the use of
        memoization, where :math:`m` and :math:`n` are the number of characters in the
        source and the pattern strings respectively

    :param str S: Source string.
    :param str P: Regex pattern.
    :param int i: Index in regex expression (used in recursion).
    :param int j: Index in source string (used in recursion).
    :return: :data:`True` if the source matches the pattern, :data:`False` otherwise.

    """
    if j == len(P):
        return i == len(S)
    else:
        f_match = i < len(S) and P[j] == S[i] or P[j] == '.'
        if j + 1 < len(P) and P[j + 1] == '*':
            return match(S, P, i, j + 2) or (f_match and match(S, P, i + 1, j))
        else:
            return f_match and match(S, P, i + 1, j + 1)
