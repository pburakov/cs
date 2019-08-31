"""
Longest Increasing Path in a Matrix
===================================

In a two-dimensional matrix or integers, find the length of a longest path of increasing
numbers. Ony vertical or horizontal moves are allowed (no diagonals).

Example::

    ([[3, 6, 7, 5],
      [2, 8, 9, 1],
      [4, 8,10, 0],
      [6, 7, 3, 9]]) -> 6  # path: 2->3->6->7->9->10)

"""


def lip(M):
    """Computes the length of the longest increasing path in a two-dimensional matrix.

    Constructs the cache and runs a DFS subroutine for every element in the matrix.

    Complexity:
        :math:`O(mn)` where :math:`m` and :math:`n` are the vertical and horizontal size of
        the matrix; :math:`O(mn)` space is used for the memoization.

    :param list[list[int]] M: Input matrix.
    :return: Length of the longest increasing path in the matrix.

    """
    cache = [[0 for _ in range(len(M[0]))] for _ in range(len(M))]
    maximum = 0
    for y in range(len(M)):
        for x in range(len(M[y])):
            longest_path(M, y, x, cache)
            maximum = max(maximum, cache[y][x])
    return maximum


def longest_path(M, y, x, cache):
    """Computes the length of the longest increasing path starting at the given coordinates.

    The path-finding routine locates the next step in four possible directions for every
    onward cell in the path. This DFS algorithm uses a cache to store computed values.

    Complexity:
        First run has a :math:`O(mn)` runtime complexity, where :math:`m` and :math:`n` are
        the vertical and horizontal size of the matrix. The use of memoization allows to
        calculate longest path exactly once for each cell. Every consecutive call with the
        same argument will give :math:`O(1)` as previously computed values are found in the
        cache. The use of cache yields a dramatic optimization over :math:`O(4^n)` if
        exploring each direction recursively.

    :param list[list[int]] M: Input matrix.
    :param int y: Starting vertical coordinate.
    :param int x: Starting horizontal coordinate.
    :param list[list[int]] cache: Memoized solutions cache.
    :return: Length of the longest increasing path in the matrix starting at the given
     coordinates.

    """
    if cache[y][x] != 0:
        return cache[y][x]
    if 0 <= y < len(M) or 0 <= x < len(M[y]):
        v = M[y][x]  # Value at (x,y)
        up, down, left, right = 0, 0, 0, 0
        if y - 1 >= 0 and M[y - 1][x] < v:
            up = longest_path(M, y - 1, x, cache)
        if x + 1 < len(M[y]) and M[y][x + 1] < v:
            right = longest_path(M, y, x + 1, cache)
        if x - 1 >= 0 and M[y][x - 1] < v:
            left = longest_path(M, y, x - 1, cache)
        if y + 1 < len(M) and M[y + 1][x] < v:
            down = longest_path(M, y + 1, x, cache)
        cache[y][x] = 1 + max(up, right, left, down)
        return cache[y][x]
    else:
        return 0
