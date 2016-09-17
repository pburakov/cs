def backtrack(M, x=None, y=None):
    """
    Matrix path recursive solver.

    Complexity: O((n+m-2)!/((n-1)!(m-1)!), or n-choose-m
    :param list[list[int]] M:
    :param int x: Vertical index (used in recursion)
    :param int y: Horizontal index (user in recursion)
    :return int: Number of paths
    """
    if x is None or y is None:  # Initialize coordinates for bottom-up solution
        x, y = len(M) - 1, len(M[0]) - 1
    if x == y == 0:
        return 1
    elif x < 0 or y < 0 or M[x][y] == 1:
        return 0
    else:
        return backtrack(M, x, y - 1) + backtrack(M, x - 1, y)


def dp(M):
    # TODO: Implement DP
    pass
