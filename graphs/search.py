"""
Graph Search Algorithms
=======================
"""
from basic.fifo import Queue, enqueue, dequeue
from graphs import Graph, Vertex, Counter


def bfs(G, s):
    """Breadth-first search of a graph.

    Breadth-first search is one of the simplest algorithms for searching a graph. It is
    also the archetype for many important graph algorithms.

    BFS is so named because it gradually expands the frontier between discovered and
    undiscovered vertices uniformly across the breadth of the frontier. That is it will
    discover all vertices at the nearest distance before discovering any vertices on
    further distances, as opposed to depth-first search.

    To keep track of the progress, BFS colors each vertex `white`, `gray` or `black`. All
    vertices start out `white`. A vertex is discovered the first time it is encountered
    during the search at which time it becomes non-white. `Gray` vertices represent the
    frontier between discovered and undiscovered vertices.

    When a vertex is discovered, BFS saves a pointer to the predecessor (or parent) vertex
    from which it was discovered, and the distance from the source vertex. BFS correctly
    computes **the shortest path**, or a minimum amount of edges it took to reach the
    vertex from a starting vertex in an unweighted graph.

    Complexity:
        :math:`O(V+E)`. :math:`V` devoted to queue operations for each vertex and
        :math:`E` time is spent on scanning adjacent vertices.

    :param Graph G: Graph to search.
    :param Vertex s: The starting vertex.

    """
    n = len(G.V)  # Total number of vertices in a graph
    # Initialize graph for the search
    for u in G.V:
        if u is not s:
            u.color = WHITE  # mark vertex as undiscovered
            u.d = inf  # reset distance
            u.p = None  # reset parent
    s.color = GRAY
    s.d = 0  # mark starting distance
    s.p = None
    Q = Queue(n)
    enqueue(Q, s)
    while Q.length != 0:
        u = dequeue(Q)
        for v in G.Adj(u):
            if v.color is WHITE:
                v.color = GRAY  # extend frontier
                v.d = u.d + 1  # calculate distance to vertex `v`
                v.p = u  # save pointer to parent
                enqueue(Q, v)
        u.color = BLACK  # finished exploring vertex `u`


def dfs(G):
    """Depth-first search of a graph.

    The strategy of depth-first search is to search deeper into the graph whenever
    possible. Once all edges of the most recently discovered vertex have been explored,
    the search **backtracks** to the next undiscovered vertex.

    Just as BFS, DFS uses colors to indicate vertices state. Whenever a vertex is visited,
    DFS also saves a pointer to the predecessor vertex, from which it was discovered.
    Instead of a distance DFS stores information about the time of discovery and the time
    at which the exploration of edges of the vertex was finished.

    DFS yields valuable information about the graph. The basic property states that the
    predecessor sub-graph forms a forest of trees encompassing the structure of recursive
    calls of :func:`dfs_visit()`. This is called the forest of depth-first trees.

    Another property states that if we print the discovery and finishing times of a
    vertex :math:`u` as expressions :math:`(u` and :math:`u)`, the resulting output makes a
    well-formed expression with properly nested parentheses.

    DFS is used to classify four edge types in the graph :math:`G`:

    - `Tree edges` are the edges in the depth-first forest traced by following the parent
      edges :math:`G.p`. An edge :math:`(u, v)` is a `tree edge` if vertex :math:`v` was
      first discovered by exploring the edge :math:`(u, v)`.
    - `Back edges` are the edges that connect a vertex to an ancestor in a depth-first
      tree. Back edges are caused by a loop in a directed graph.
    - `Forward edges` are edges that connect a vertex to a descendant in a depth-first
      tree, like a "shortcut".
    - `Cross edges` are all other edges. They connect subtrees, or can go between vertices
      in the same subtree, as long as one connected vertex is not a descendant of the other.

    Forward and cross edges never occur in a DFS of an undirected graph.

    Note that this implementation of DFS has no arbitrary starting point. The search is
    performed on all connected vertices present in a Graph, although it should be trivial
    to update the algorithm to perform a local DFS.

    Complexity:
        :math:`O(V+E)`, no additional space is used.

    :param Graph G: Graph to search.

    """
    t = Counter()  # Mutable counter
    # Initialize graph for the search
    for u in G.V:
        u.color = WHITE  # mark vertex as undiscovered
        u.p = None  # reset parent
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
        :math:`O(d)` where :math:`d` is a degree of the vertex.

    :param Graph G: Graph to search.
    :param Vertex u: Vertex to visit.
    :param Counter t: Distance ticker.

    """
    t.tick += 1
    u.d = t.tick  # save discovery time of vertex `u`
    u.color = GRAY  # mark discovered
    for v in G.Adj(u):  # Explore `u`'s edges
        if v.color is WHITE:
            v.p = u  # save pointer to parent
            dfs_visit(G, v, t)  # Recursively visit adjacent vertex
    u.color = BLACK  # vertex is finished
    t.tick += 1
    u.f = t.tick  # Saving finishing time of vertex `u`
