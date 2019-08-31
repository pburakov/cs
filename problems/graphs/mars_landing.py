"""
Mars Lander
===========

You’re in charge of sending a lander to Mars. You have a map of the surface — a grid sized
:math:`m \\times n`. The surface is uneven. It has flat areas as well as impassable rocky
areas. Your lander has :math:`p` rovers on-board. Each rover can travel the shortest route
at a constant speed to any tile, where it will remain for a scientific survey of the soil.
A rover can move to an adjacent horizontal or vertical tile, unless the tile contains a
rocky area, consuming exactly one gallon of fuel on every move.

You are given a set of coordinates :math:`P=\{(x_1,y_1),(x_2,y_2)...(x_p,y_p)\}`, which
your rovers will need to survey. You are also given a two-dimensional array :math:`M`,
representing the map grid. On this grid, the impassable rocky areas are encoded with a
character ``"X"``, and normal tiles are encoded with a character ``"-"``. The lander needs
to carry enough fuel for the rovers to reach all available survey areas, but unfortunately,
the weight your lander can hold is limited.

Find such landing site with coordinates :math:`(x, y)` so that the fuel consumption for the
rovers on board is minimal. Refrain from landing directly on a survey area tile, as the
rocket fuel may contaminate the soil.

Example::

    (M = [['-', 'X', 'X', '-'],
          ['-', '-', 'X', '-'],
          ['-', '-', '-', '-'],
          ['-', '-', '-', '-']], P=[(0, 0), (0, 3), (3, 1)]) -> (2, 1)

I was given this problem when I was interviewing at Google. Below is my stab at it.

"""


def landing_site(M, P):
    """Returns the coordinates of an optimal site for landing.

    The idea is to measure distances by building distance maps (fuel cost) from each
    survey point to every potential landing location. The best candidate for a landing
    would be the tile with a minimal sum of those distances.

    The algorithm assumes that all survey points are reachable and no region is completely
    blocked by rocks.

    Complexity:
        :math:`O(p(mn-x)+mn)` where :math:`p` is number of probes; :math:`m` and :math:`n`
        are the vertical and horizontal size of the map, and :math:`x` is the number of
        unpassable rocky tiles.

    :param list[list[str]] M: Map of Mars' surface.
    :param list[tuple] P: Survey points.
    :return: Coordinates of a proposed landing site.

    """
    m, n = len(M), len(M[0])
    fuel = init_dist_map(m, n)
    for (y, x) in P:
        p_distances = init_dist_map(m, n)
        build_dist_map(M, p_distances, y, x)
        # Sum up estimated fuel consumption for each landing location
        fuel = [[(fuel[i][j] + p_distances[i][j]) for j in range(n)] for i in range(m)]
    for y, x in P:
        fuel[y][x] = 0  # Can't land on a survey point
    # Find minimal distance
    m_y, m_x, min_fuel = 0, 0, inf
    for y in range(m):
        for x in range(n):
            if 0 < fuel[y][x] < min_fuel:
                min_fuel = fuel[y][x]
                m_y, m_x = y, x
    return m_y, m_x


inf = float("inf")


def build_dist_map(M, distance_map, y, x):
    """Calculated a distance map for a starting point.

    This BFS-like subroutine puts distances to tile :math:`(x, y)` from all other tile.
    Distance gets larger as tile is further away from the starting point. Tiles containing
    ``"X"`` are excluded.

    Complexity:
        :math:`O(mn-x)` where :math:`m` and :math:`n` are the vertical and horizontal size
        of the map, and `x` is the number of impassable rocky tiles.

    :param list[list[str]] M: Input map.
    :param list[list[int]] distance_map: Mutable distance map.
    :param int y: Vertical coordinate of a target tile.
    :param int x: Horizontal coordinate of a target tile.

    """
    from queue import Queue
    q = Queue()
    q.put((y, x))
    while q.empty() is False:
        (p_y, p_x) = q.get()
        d = distance_map[p_y][p_x]  # Distance at (p_x,p_y)
        for v_y, v_x in adj(M, p_y, p_x):
            if M[v_y][v_x] != 'X' and distance_map[v_y][v_x] == 0:
                distance_map[v_y][v_x] = d + 1
                q.put((v_y, v_x))


def init_dist_map(m, n):
    """Builds a two-dimensional matrix with zero values.

    Complexity:
        :math:`O(mn)`.

    :param int m: Vertical size.
    :param int n: Horizontal size.
    :return: A two-dimensional matrix with zero values.

    """
    return [[0 for _ in range(n)] for _ in range(m)]


def adj(M, y, x):
    """Generates coordinates of adjacent tiles.

    Will yield at most four adjacent coordinates.

    Complexity:
        :math:`O(1)`.

    :param list[list[str]] M: Input map.
    :param int y: Vertical coordinate of a source tile.
    :param int x: Horizontal coordinate of a source tile.
    :return: Coordinates of a next adjacent tile.

    """
    if y - 1 >= 0:
        yield y - 1, x
    if x + 1 < len(M[y]):
        yield y, x + 1
    if y + 1 < len(M):
        yield y + 1, x
    if x - 1 >= 0:
        yield y, x - 1
