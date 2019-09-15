"""
Paths in Matrix
===============

Given a 2-D array :math:`M` sized :math:`m \\times n`, find the number of ways to reach the
bottom right corner from the top left corner by moving strictly right or down. Cells with a
value of :math:`1` cannot be traversed.

Example::

    paths([[0, 0, 1],
           [0, 0, 0],
           [1, 0, 0]]) -> 4

This is a combinatorial problem that also has all the necessary properties for a dynamic
programming solution.
"""


def backtrack(M, x=None, y=None):
    """Matrix path recursive solver.

    Imagine that we're solving this problem for the matrix of size :math:`4\\times3` with
    only free cells. Observe that any path will take :math:`n+m-2=5` moves corner-to-corner.
    For example: `DDRRR`, `RRRDD`, `RDRDR` and so on, where `D` is down, `R` is right.
    Observe that each route will have a set of 3 `R`'s and 2 `D`'s in various permutations.

    If a matrix had nothing but the free cells, the solution would be as easy as solving
    n-choose-k formula: :math:`\\frac{(n+m-2)!}{(n-1)!(m-1)!}=\\frac{5!}{3!2!} = 10`.
    Since some of the cells are not traversable, we can use backtracking to reduce the
    number of possible moves.

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
    :return: Integer number of paths.

    """
    if x is None or y is None:  # Initialize coordinates for bottom-up solution
        x, y = len(M) - 1, len(M[0]) - 1
    if x == y == 0:  # Destination
        return 1
    elif x < 0 or y < 0 or M[x][y] == 1:  # Edge
        return 0
    else:  # Free cell, two options where to move
        return backtrack(M, x, y - 1) + backtrack(M, x - 1, y)
