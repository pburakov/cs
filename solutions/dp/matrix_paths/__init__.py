def backtrack(M, x=None, y=None):
    """
    Matrix path recursive solver.

    Imagine that we're solving this problem for the matrix of size `4`x`3` with only free
     cells. Observe that any path will take `m + n - 2 = 5` moves corner-to-corner, for
     example: DDRRR, RRRDD, RDRDR (D=down, R=right) and so on. Observe that each route
     will have 2 D's and 3 R's. Which looks like a permutation problem.

    If matrix has nothing but free cells (no `1`s), the solution would be as easy as
     solving n-choose-k forumla: `5!/(2!3!) = 10`. Since some of the cells are not
     traversable we can solve it using backtracking for a reduced number of possible
     moves.

    We have only three cases:
     a) we reached destination
     b) we reached an edge
     c) we move right or down

    Complexity: O((n+m-2)!/((n-1)!(m-1)!), is proportional to the output, or n-choose-m
     formula for combinations without repetitions.
    :param list[list[int]] M:
    :param int x: Vertical index (used in recursion)
    :param int y: Horizontal index (user in recursion)
    :return int: Number of paths
    """
    if x is None or y is None:  # Initialize coordinates for bottom-up solution
        x, y = len(M) - 1, len(M[0]) - 1
    if x == y == 0:  # Destination
        return 1
    elif x < 0 or y < 0 or M[x][y] == 1:  # Edge
        return 0
    else:  # Free cell, two options where to move
        return backtrack(M, x, y - 1) + backtrack(M, x - 1, y)


def dp(M):
    # TODO: Implement DP
    pass
