"""
Count Islands
=============

The input is a 2-D matrix :math:`M` of integers :math:`0` and :math:`1`. Let :math:`1`
represent a tile of land. A group of vertically and horizontally connected land tiles forms
an island. Count the number of "islands" on a map.

Example::

    M = [[0, 0, 0, 1, 1],
         [1, 1, 0, 0, 1],
         [0, 1, 0, 1, 1],
         [0, 0, 0, 0, 1],
         [0, 0, 1, 0, 0]]

    count(M) -> 3

"""


def solution(M):
    """Count Islands problem solver.

    This is a variation of a solution strongly connected components of a DAG. The problem
    can be easily solved by applying DFS on each component. In each DFS call, a component
    or a sub-graph is visited. If we keep track of visited tiles and count the number of
    calls to DFS we'll get the count of connected components. BFS can also be used.

    Complexity:
        :math:`O(V+E')` where :math:`E'` is number of edges within "islands".

    :param list[list[int]] M: Input map.
    :return: Integer count of islands.

    """
    count = 0  # Output counter
    visited = {}  # Hash map of visited coordinates
    m = len(M)  # Vertical size
    for i in range(0, m):
        n = len(M[i])  # Horizontal size
        for j in range(0, n):
            if M[i][j] == 1 and (i, j) not in visited:
                # Runs DFS search and marks island tiles as visited
                explore(M, i, j, visited)
                count += 1
    return count


"""
Auxiliary routines used in the solution
"""


def adj(M, y, x):
    """Generator of coordinates of adjacent island tiles.

    Complexity:
        :math:`O(1)`. Will yield 4 adjacent coordinates.

    :param list[list[int]] M: Input map.
    :param int y: Vertical coordinate.
    :param int x: Horizontal coordinate.
    :return: Coordinates of next adjacent land tile

    """
    if y - 1 > 0 and M[y - 1][x] == 1:
        yield y - 1, x
    if y + 1 < len(M) and M[y + 1][x] == 1:
        yield y + 1, x
    if x - 1 > 0 and M[y][x - 1] == 1:
        yield y, x - 1
    if x + 1 < len(M[y]) and M[y][x + 1] == 1:
        yield y, x + 1


def explore(M, y, x, visited):
    """DFS subroutine for exploring islands.

    Complexity:
        :math:`O(V'+E')` where :math:`V'` is number of tiles in within the island and
        :math:`E'` is number of edges connecting them.

    :param list[list[int]] M: Input map.
    :param int y: Starting vertical coordinate.
    :param int x: Starting horizontal coordinate.
    :param dict[tuple] visited: Mutable hash map (:data:`dict`) of coordinates of visited
     tiles.

    """
    if M[y][x] == 1 and (y, x) not in visited:
        visited[(y, x)] = True
        for i, j in adj(M, y, x):
            explore(M, i, j, visited)
