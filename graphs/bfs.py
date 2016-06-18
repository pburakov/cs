from graphs.graph import Graph, Vertex
from basic_data_structures.queue import Queue, enqueue, dequeue


def bfs(G, s):
    """
    Breadth-first search is one of the simplest algorithms for searching a graph.
     It is also the archetype for many important graph algorithms.

    BFS is so named because it gradually expands the frontier between discovered
     and undiscovered vertices uniformly across the breadth of the frontier. That
     is it will discover all vertices at the nearest distance before discovering
     any vertices on further distances, as opposed to depth-first search.

    To keep track of the progress BFS colors each vertex white, gray or black.
     All vertices start out white. A vertex is discovered the first time it is
     encountered during the search at which time it becomes nonwhite. All vertices
     adjacent to black vertices have been discovered while gray vertices may have
     adjacent white vertices. Gray vertices represent the frontier between discovered
     and undiscovered vertices.

    When vertex is discovered BFS writes pointer to a predecessor (or parent) vertex
     and the distance from the source vertex. That said BFS correctly computes the
     shortest path or a minimum amount of edges it took to reach the vertex from the
     starting vertex.

    Complexity: O(V+E). `V` devoted to queue operations for each vertex and `E` is
     for the total time spent on scanning adjacent vertices.
    :param Graph G: Adjacency list graph representation
    :param Vertex s: Pointer to the starting vertex
    :return None: Vertices are updated
    """
    n = len(G.V)  # Total number of vertices in a graph

    for u in G.V:
        if u != s:
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
        for v in u.Adj:
            if v.color == WHITE:
                v.color = GRAY
                v.d = u.d + 1
                v.p = u
                enqueue(Q, v)
        u.color = BLACK


"""
Constants used in BFS
"""
WHITE = "WHITE"
GRAY = "GRAY"
BLACK = "BLACK"
inf = float("inf")
