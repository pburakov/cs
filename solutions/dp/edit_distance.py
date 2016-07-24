"""
In computer science, edit distance is a way of quantifying how dissimilar two strings
 are to one another by counting the minimum number of operations required to transform
 one string into the other.

You are given a source string `S` and a target string `T`. Three types of operations are
 possible, let `1` be the equal cost of each:
 - *replace* (substitute) character in string `S` with a character from string `T`.
 - *insert* a character into string `S` to help it match string `T`.
 - *delete* a character from string `S`.

Find minimum amount of edits required to transform `S` into `T`. For example, edit
 distance of string "cat" and "nuts" is 3 (add `s`, replace `a` with `u`, replace `c`
 with `n`).

This algorithm is used in spell checkers and to quantify the similarity of DNA
 sequences. It is described in great detail in the book "Algorithm Design Manual" by
 S. Skiena.
"""


def backtrack(S, T, i=None, j=None):
    """
    Edit distance solver using recursion.

    Please note, that we don't need to perform and string modifications, only compute
     the cost. We can define a recursive algorithm using the observation that the last
     character in the string must either be matched, substituted, inserted or deleted.
     If we knew the costs associated with these edits we could decide which option leads
     to the best solution.

    This is a top-down approach, although correct, it is impossibly slow, at every
     position in the string the recursion branches three ways. There are several
     subroutines used here to improve the clarity of the code.

    Complexity: O(3^n), recursion grows at a rate of at least 3^n, even faster.
    :param str S: Source string
    :param str T: Target string
    :param int i: Pointer index in `S` (used in recursion)
    :param int j: Pointer index in `T` (used in recursion)
    :return int: Edit distance between `S` and `T`
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
        return backtrack(S, T, i - 1, j - 1)  # No added cost
    else:
        return COST + min(
            backtrack(S, T, i - 1, j - 1),
            backtrack(S, T, i, j - 1),
            backtrack(S, T, i - 1, j)
        )


def dp(S, T):
    """
    Edit distance solver using DP.

    Just like we saw in other dynamic programming problems, this solution is built in a
     bottom-up fashion. It computes and memoizes the optimal results in a table and each
     next decision resides on top of optimally solved sub-problems. When completed, `DP`
     table will look like this:
     ```
         'n' 'u' 't' 's'
     'c'  1   1   1   1
     'a'  1   2   2   2
     't'  1   2   2   3  <- the goal
     ```
    The DP solution uses same subroutines as the recursive solution. Additionally we can
     store the history of decisions in auxiliary table, that can be used to rebuild
     intermediate transformations of the string `S` (not implemented).

    Complexity: O(nm). Use of dynamic programming allows us to upgrade the speed of this
     algorithm to polynomial time, sacrificing O(mn) space.
    :param str S: Source string
    :param str T: Target string
    :return int: Edit distance between `S` and `T`
    """
    m = len(S)
    n = len(T)
    DP = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(0, m + 1):
        for j in range(0, n + 1):
            # The logic of populating the table is the same as recursive approach
            a, b = S[i - 1], T[j - 1]
            if i == 0:
                DP[i][j] = j * COST
            elif j == 0:
                DP[i][j] = i * COST
            elif a == b:
                DP[i][j] = DP[i - 1][j - 1]  # No added cost
            else:
                DP[i][j] = COST + min(
                    DP[i - 1][j - 1],
                    DP[i][j - 1],
                    DP[i - 1][j]
                )
    return DP[m][n]


"""
Constants used in the solution
"""
inf = float("inf")
COST = 1
