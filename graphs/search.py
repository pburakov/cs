"""
Graph Search Algorithms
=======================
"""
from basic_data_structures.fifo import Queue, enqueue, dequeue
from graphs import Graph, Vertex


def bfs(G, s):
    """Breadth-first search of a graph.

    Breadth-first search is one of the simplest algorithms for searching a graph. It is
    also the archetype for many important graph algorithms.

    BFS is so named because it gradually expands the frontier between discovered and
    undiscovered vertices uniformly across the breadth of the frontier. That is it will
    discover all vertices at the nearest distance before discovering any vertices on
    further distances, as opposed to depth-first search.

    To keep track of the progress BFS colors each vertex `white`, `gray` or `black`. All
    vertices start out `white`. A vertex is discovered the first time it is encountered
    during the search at which time it becomes non-white. `Gray` vertices represent the
    frontier between discovered and undiscovered vertices.

    When vertex is discovered BFS saves a pointer to the predecessor (or parent) vertex
    from which it was discovered, and the distance from the source vertex. BFS correctly
    computes the shortest path, or a minimum amount of edges it took to reach the vertex
    from the starting vertex in an unweighted graph. If we follow parent records in a
    breadth-first tree after BFS was finished all the way to the starting vertex we'll get
    the shortest route it would take to reach the destination vertex.

    Complexity:
        :math:`O(V+E)`. :math:`V` devoted to queue operations for each vertex and
        :math:`E` is for the total time spent on scanning adjacent vertices.

    :param Graph G: Adjacency list graph representation.
    :param Vertex s: Pointer to the starting vertex.

    """
    n = len(G.V)  # Total number of vertices in a graph
    for u in G.V:
        if u is not s:
            u.color = WHITE
            u.d = inf
            u.p = None
    s.color = GRAY
    s.d = 0
    s.p = None
    Q = Queue(n)
    enqueue(Q, s)
    while Q.length != 0:
        u = dequeue(Q)
        for v in G.Adj(u):
            if v.color is WHITE:
                v.color = GRAY
                v.d = u.d + 1
                v.p = u
                enqueue(Q, v)
        u.color = BLACK


def dfs(G):
    """Depth-first search of a graph.

    The strategy of depth-first search is to search deeper in the graph whenever possible.
    Once all the edges of the most recently discovered vertex have been explored, the
    search backtracks to the next undiscovered vertex.

    Just as BFS, DFS uses colors to indicate vertices state. Whenever a vertex is visited,
    DFS also saves a pointer to the predecessor vertex, from which it was discovered.
    Instead of a distance DFS stores information about the time of discovery and the time
    at which exploring edges of a vertex was finished.

    DFS yields valuable information about the graph. The most basic property is that the
    predecessor sub-graph forms a forest of trees mirrored exactly by the structure of
    recursive calls of :func:`dfs_visit()`. It is also called the forest of depth-first
    trees.

    Another property is that if we replace discovery and finishing times of vertex
    :math:`u` with symbols :math:`(u` and :math:`u)`, the history makes a well-formed
    expression with properly nested parentheses.

    DFS can be used to classify four edge types in the graph :math:`G`:

    - `Tree edges` are the edges in the depth-first forest traced by following pointers
      :math:`G.p`. Edge :math:`(u, v)` is a `tree edge` if it was first discovered by
      exploring edge :math:`(u, v)`.
    - `Back edges` are the edges that connect a vertex to an ancestor in a depth-first
      tree. Back edges cause a loop in a directed graph (or vise versa).
    - `Forward edges` are edges that connect a vertex to a descendant in a depth-first
      tree, like a "shortcut".
    - `Cross edges` are all other edges. They can go between vertices in the same
      tree/forest as long as one connected vertex is not a descendant of the other.

    Forward and cross edges never occur in a DFS of an undirected graph.

    Note that this implementation of DFS has no arbitrary starting point. Search is
    performed on all vertices present in adjacency list, although it should be trivial to
    alter the code to perform a local DFS.

    Complexity:
        :math:`O(V+E)`, no additional space is used.

    :param Graph G: Adjacency list graph representation.

    """
    t = Counter()  # Mutable counter
    for u in G.V:
        u.color = WHITE
        u.p = None
    for u in G.V:
        if u.color is WHITE:
            dfs_visit(G, u, t)


"""
Constants and subroutines used in graph search
"""
WHITE = "WHITE"  # Unvisited
GRAY = "GRAY"  # Discovered
BLACK = "BLACK"  # Visited
inf = float("inf")


def dfs_visit(G, u, t):
    """DFS vertex visit procedure.

    Complexity:
        :math:`O(Adj)` where :math:`Adj` is number of adjacent vertices.

    :param Graph G: Adjacency list graph representation.
    :param Vertex u: Vertex to visit.
    :param Counter t: Mutable timer (integer counter).

    """
    t.tick += 1
    u.d = t.tick  # Saving discovery time of vertex `u`
    u.color = GRAY
    for v in G.Adj(u):  # Explore `u`'s edges
        if v.color is WHITE:
            v.p = u
            dfs_visit(G, v, t)  # Recursively visit adjacent vertex
    u.color = BLACK
    t.tick += 1
    u.f = t.tick  # Saving finishing time of vertex `u`


class Counter:
    """Simple mutable counter object.
    """

    def __init__(self, t=0):
        """Simple mutable counter object.

        :param int t: Starting number.

        """
        self.tick = t
