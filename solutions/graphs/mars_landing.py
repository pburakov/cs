"""
Imagine you are sending a lander to Mars. Your lander has `p` probes on-board that can
 travel the shortest route at constant speed to designated points of interest for a
 scientific survey and then back following the same path. You are given map of surface
 sized `m`x`n`, where `-` are normal tiles and `x` are rocky tiles that are impassable.
 You are also given `p` sets of coordinates `P` for all your probes. Your probes can move
 to adjacent horizontal and vertical tile, consuming 1 unit of fuel on every move. Find
 such a landing position for your lander so that the fuel consumption for all `p` probes
 is minimal. Assume that all points are reachable (not blocked by rocks).

Example:
```p=3; P=[(0, 0), (0, 3), (3, 1)]
M = [
    ['-', 'x', 'x', '-'],
    ['-', '-', 'x', '-'],
    ['-', '-', '-', '-'],
    ['-', '-', '-', '-'],
]
Best landing site: (2, 1).
```
I was given this problem when I was interviewing at Google. Here is my stab at it.
"""


def find_landing(M, P):
    """
    Mars landing solver.

    The idea is to measure distances by building distance maps (fuel cost) for each
     survey point. Finding point with a minimal sum of those distances will be the best
     candidate for a landing.

    Algorithm assumes that all survey points are reachable and no region is completely
     blocked by rocks.

    Complexity: O(p(mn-x)+mn) where `p` is number of probes, `mn` is the total number of
     map tiles and `x` is the number of unpassable rocky tiles.
    :param list[list[str]] M: Map of surface
    :param list[tuple] P: Points of interest
    :return tuple: Coordinates of proposed landing site
    """
    m, n = len(M), len(M[0])
    fuel = init_dist_map(m, n)
    for (x, y) in P:
        p_distances = init_dist_map(m, n)
        build_dist_map(M, p_distances, x, y)
        fuel = [[(fuel[i][j] + p_distances[i][j]) for j in range(n)] for i in range(m)]
    for x, y in P:
        fuel[x][y] = 0  # Can't land on survey point
    # Find minimal distance
    m_x, m_y, min = 0, 0, inf
    for i in range(m):
        for j in range(n):
            if 0 < fuel[i][j] < min:
                min = fuel[i][j]
                m_x, m_y = i, j
    return m_x, m_y


"""
Auxiliary constants and routines used in the solution
"""
inf = float("inf")


def build_dist_map(M, distance_map, x, y):
    """
    Populates distance map from a starting point.

    This is a traditional bread-first search subroutine that puts distances to point
     `(x, y)` from any other point. Similar to inverse heat map, distance gets larger as
     BFS gets further away from the starting point. Rocky formations are excluded.

    Complexity: O(mn-x) where `mn` is the total number of tiles and `x` is number of
     unpassable rocky tiles.
    :param list[list[str]] M: Input map
    :param list[list[int]] distance_map: Distance map
    :param int x: Vertical axis coordinate of a starting point
    :param int y: Horizontal axis coordinate of a starting point
    :return None: Distance map `R` is updated
    """
    from queue import Queue
    q = Queue()
    q.put((x, y))
    while q.empty() is False:
        (p_x, p_y) = q.get()
        d = distance_map[p_x][p_y]  # Distance at `p_x`, `p_y`
        for v_x, v_y in adj(M, p_x, p_y):
            if M[v_x][v_y] != 'x' and distance_map[v_x][v_y] == 0:
                distance_map[v_x][v_y] = d + 1
                q.put((v_x, v_y))


def init_dist_map(m, n):
    """
    Initializes two-dimensional matrix, containing only zeroes.

    Complexity: O(mn)
    :param int m: Vertical size
    :param int n: Horizontal size
    :return list[list[int]]: Empty distances map
    """
    return [[0 for _ in range(n)] for _ in range(m)]


def adj(M, x, y):
    """
    Generator of coordinates of adjacent tiles within bounds.

    Complexity: O(1). Will yield 4 adjacent coordinates.
    :param list[list[str]] M: Input map
    :param int x: Vertical axis coordinate
    :param int y: Horizontal axis coordinate
    :return __generator[int, int]: Coordinates of next adjacent tile
    """
    if x - 1 >= 0:
        yield x - 1, y
    if y + 1 < len(M[x]):
        yield x, y + 1
    if x + 1 < len(M):
        yield x + 1, y
    if y - 1 >= 0:
        yield x, y - 1
