"""
Edit Distance
=============

In computer science, edit distance (**Levenstein** distance) is a way of quantifying how
dissimilar two strings are to one another by counting the minimum number of operations
required to transform one string into the other.

You are given a source string :math:`S` and a target string :math`T`. Three types of
operations are possible, let :math:`1` be the equal cost of each:

    - *replace* (substitute) character in string :math:`S` with a character from string
      :math:`T`;
    - *insert* a character into string :math:`S` to help it match string :math:`T`;
    - *delete* a character from string :math:`S`.

Find minimum amount of edits required to transform :math:`S` into :math:`T`. For example,
the edit distance of string "cat" and "nuts" is :math:`3` (add `s`, replace `a` with `u`,
replace `c` with `n`).

Example::

    ("cat", "nuts") -> 3

The algorithm solving this problem is used in spell checkers and to quantify the similarity
of DNA sequences. It is described in great detail in the book *Algorithm Design Manual* by
S. Skiena.
"""


def edit_distance(S, T, i=None, j=None):
    """Calculates the edit distance between the source and the target string.

    We can define a recursive algorithm using the observation that the last character in the string must either be matched, substituted, inserted or deleted. If we knew the costs associated with these edits we could decide which option leads to the best solution.

    This top-down approach, although correct, it is impossibly slow. At every position in the string, the recursion branches three ways.

    Complexity:
        :math:`O(3^n)` due to recursion growth rate.

    :param str S: Source string.
    :param str T: Target string.
    :param int i: Pointer index in :math:`S` (used in recursion).
    :param int j: Pointer index in :math:`T` (used in recursion).
    :return: Edit distance between strings.

    """
    if i is None or j is None:  # Initializing pointers
        i = len(S)
        j = len(T)
    if i == 0:
        return j * COST
    if j == 0:
        return i * COST
    a, b = S[i - 1], T[j - 1]  # Pick next two characters to compare
    if a == b:
        return edit_distance(S, T, i - 1, j - 1)  # No added cost
    else:
        return COST + min(
            edit_distance(S, T, i - 1, j - 1),
            edit_distance(S, T, i, j - 1),
            edit_distance(S, T, i - 1, j)
        )


def edit_distance_dp(S, T):
    """Calculates the edit distance between the source and the target string.

    Just like we saw in other dynamic programming problems, this solution is built in a
    bottom-up fashion. It computes and memoizes the optimal result in a table, and each
    next decision resides on top of previously solved results.

    For example, when completed for words  `cat` and `nuts`, the cache will look like
    this::

         'n' 'u' 't' 's'
     'c'  1   1   1   1
     'a'  1   2   2   2
     't'  1   2   2   3  <- the goal

    Note how the subroutines used here are the same as in the recursive solution.

    Complexity:
        :math:`O(nm)`. Use of dynamic programming allows us to dramatically improve the
        speed of the same algorithm to polynomial time, sacrificing :math:`O(mn)` space.

    :param str S: Source string.
    :param str T: Target string.
    :return: Edit distance between strings.

    """
    m = len(S)
    n = len(T)
    cache = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(0, m + 1):
        for j in range(0, n + 1):
            # The logic of populating the table is the same as recursive approach
            if i == 0:
                cache[i][j] = j * COST
            elif j == 0:
                cache[i][j] = i * COST
            elif S[i - 1] == T[j - 1]:
                cache[i][j] = cache[i - 1][j - 1]  # No added cost
            else:
                cache[i][j] = COST + min(
                    cache[i - 1][j - 1],
                    cache[i][j - 1],
                    cache[i - 1][j]
                )
    return cache[m][n]


"""
Constants used in the solution
"""
inf = float("inf")
COST = 1
