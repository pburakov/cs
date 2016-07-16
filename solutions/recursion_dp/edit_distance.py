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
 distance of string "cat" and "nuts" is 2 (add `s`, replace `a` with `u`, replace `c`
 with `n`).

This algorithm is used in spell checkers and quantify the similarity of DNA sequences.
 It is described in detail in the book "Algorithm Design Manual" by S. Skiena.
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
        b = T[j - 1]
        return j * cost_insert(b)
    if j == 0:
        a = S[i - 1]
        return i * cost_delete(a)
    a, b = S[i - 1], T[j - 1]  # Pick next two characters to compare
    return min(
        backtrack(S, T, i - 1, j - 1) + cost_replace(a, b),
        backtrack(S, T, i, j - 1) + cost_insert(b),
        backtrack(S, T, i - 1, j) + cost_delete(a)
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
     't'  1   2   2   3

    The DP solution uses same subroutines as the recursive solution with the addition of
     `find_goal()` subroutine that will find the maximum value in the table, since the
     cheapest place to match the entire pattern is not necessarily at the end of both
     string. Additionally we can store the history of decisions in auxiliary table, that
     can be used to rebuild intermediate transformations of the string `S`.

    :param str S: Source string
    :param str T: Target string
    :return int: Edit distance between `S` and `T`
    """
    m = len(S)
    n = len(T)
    if m == 0:
        return n * cost_insert('')
    if n == 0:
        return m * cost_delete('')
    DP = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(0, m):
        for j in range(0, n):
            a = S[i]
            b = T[j]
            DP[i][j] = min(
                DP[i - 1][j - 1] + cost_replace(a, b),
                DP[i][j - 1] + cost_insert(b),
                DP[i - 1][j] + cost_delete(b)
            )
    y, x = find_goal(DP)
    return DP[y][x]


"""
Auxiliary methods and constants used in the solution
"""
inf = float("inf")


def cost_replace(x, y):
    """
    Returns the cost of replacement of two characters in a string.

    Complexity: O(1)
    :param str x: First character
    :param str y: Second character
    :return int: Cost of replacement
    """
    if x == y:
        return 0  # No need for a substitution
    else:
        return 1


def cost_insert(x):
    """
    Returns the cost of insertion of an arbitrary character into a string.

    Complexity: O(1)
    :param str x: Subject character
    :return int: Cost of insertion
    """
    return 1


def cost_delete(x):
    """
    Returns the cost of deletion of an arbitrary character from a string.

    Complexity: O(1)
    :param str x: Subject character
    :return int: Cost of deletion
    """
    return 1


def find_goal(T):
    """
    Returns indexes of largest element in a matrix.

    Complexity: O(mn)
    :param list[list] T: Two-dimensional array (list) or positive integers
    :return tuple: Output indexes
    """
    max = -inf
    y, x = 0, 0
    m = len(T)
    for i in range(0, m):
        n = len(T[i])
        for j in range(0, n):
            if T[i][j] >= max:
                max = T[i][j]
                y, x = i, j
    return y, x
