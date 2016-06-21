from graphs.graph import Graph, Vertex


def dfs(G):
    """
    Depth-first search of a graph

    The strategy of depth-first search is to search deeper in the graph whenever
     possible. Once all the edges of the most recently discovered vertex have been
     explored, the search backtracks to the next undiscovered vertex.

    Just as BFS, DFS uses colors to indicate vertices state. Whenever a vertex is
     visited, DFS also saves a pointer to the predecessor vertex, from which it was
     discovered. Instead of a distance DFS stores information about the time of
     discovery and the time at which exploring edges of a vertex was finished.

    DFS yields valuable information about the graph. The most basic property is that
     the predecessor sub-graph forms a forest of trees mirrored exactly by the
     structure of recursive calls of `dfs_visit()`. It is also called the forest of
     depth-first trees.

    Another property is that if we replace discovery and finishing times of vertex `u`
     with symbols `(u` and `u)`, the history makes a well-formed expression with
     properly nested parentheses.

    DFS can be used to classify four edge types in the graph `G`:
     1. Tree edges are the edges in the depth-first forest `G.p`. Edge (u, v) is a
      tree edge if it was first discovered by exploring edge (u, v).
     2. Back edges are edges that connect a vertex to an ancestor in a depth-first
      tree. Back edges cause a loop in a directed graph (or vise versa).
     3. Forward edges are edges that connect a vertex to a descendant in a depth-
      first tree, like a "shortcut".
     4. Cross edges are all other edges. They can go between vertices in the same
      tree/forest as long as one connected vertex is not a descendant of the other.
     Forward and cross edges never occur in a DFS of an undirected graph.

    Note that this implementation of DFS has no arbitrary starting point. Search is
     performed on all vertices present in adjacency list, although it should be
     trivial to alter the code to perform a local DFS.

    Complexity: O(V+E), no additional space is used.
    :param Graph G: Adjacency list graph representation
    :return None: Vertices are updated
    """
    t = Timer()  # Mutable counter

    for u in G.V:
        u.color = WHITE
        u.p = None
    for u in G.V:
        if u.color is WHITE:
            dfs_visit(G, u, t)


def dfs_visit(G, u, t):
    """
    Vertex visit procedure

    Complexity: O(Adj) where `Adj` is number of adjacent vertices
    :param Graph G: Adjacency list graph representation
    :param Vertex u: Vertex to visit
    :param Timer t: Mutable timer (integer counter)
    :return None: Vertex `u` and adjacent vertices are updated
    """
    t.tick += 1
    u.d = t.tick  # Saving discovery time of vertex `u`
    u.color = GRAY
    for v in u.Adj:  # Explore `u`'s edges
        if v.color is WHITE:
            v.p = u
            dfs_visit(G, v, t)  # Recursively visit adjacent vertex
    u.color = BLACK
    t.tick += 1
    u.f = t.tick  # Saving finishing time of vertex `u`


"""
Constants and auxiliary objects used in DFS
"""
WHITE = "WHITE"  # Unvisited
GRAY = "GRAY"    # Discovered
BLACK = "BLACK"  # Visited


class Timer:
    def __init__(self, t=0):
        """
        Simple mutable counter object

        :param int t: Starting number
        """
        self.tick = t
