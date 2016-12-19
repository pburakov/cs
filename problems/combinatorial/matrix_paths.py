"""
Paths in Matrix
===============

Given a 2-D array :math:`M` sized :math:`m \\times n`, find number of ways to get from the
top left corner to the bottom right corner by moving strictly right or down. Cells with a
value of :math:`1` cannot be traversed.

Example::

    M = [[0, 0, 1],
         [0, 0, 0],
         [1, 0, 0]]

    paths(M) -> 4

This is a combinatorial problem that also has the necessary properties for a dynamic
programming solution.
"""


def backtrack(M, x=None, y=None):
    """Matrix path recursive solver.

    Imagine that we're solving this problem for the matrix of size `4`x`3` with only free
    cells. Observe that any path will take `m + n - 2 = 5` moves corner-to-corner, for
    example: DDRRR, RRRDD, RDRDR (D=down, R=right) and so on. Observe that each route will
    have 2 D's and 3 R's. Which looks like a permutation problem.

    If matrix has nothing but free cells (no `1`s), the solution would be as easy as
    solving n-choose-k forumla: `5!/(2!3!) = 10`. Since some of the cells are not
    traversable we can solve it using backtracking for a reduced number of possible moves.

    We have only three cases:

        A. We reached destination;
        B. We reached an edge;
        C. We move right or down.

    Complexity:
        :math:`O(\\frac{(n+m-2)!}{((n-1)!(m-1)!})`, same as the size of the output, or
        *n-choose-m* formula for combinations without repetitions.

    :param list[list[int]] M: Input matrix.
    :param int x: Vertical index (used in recursion).
    :param int y: Horizontal index (user in recursion).
    :return Integer number of paths.

    """
    if x is None or y is None:  # Initialize coordinates for bottom-up solution
        x, y = len(M) - 1, len(M[0]) - 1
    if x == y == 0:  # Destination
        return 1
    elif x < 0 or y < 0 or M[x][y] == 1:  # Edge
        return 0
    else:  # Free cell, two options where to move
        return backtrack(M, x, y - 1) + backtrack(M, x - 1, y)
