"""
Graph is a linked data structure comprised of vertices (nodes or points) and edges
 (lines, arrows or arcs) representing relationships between vertices.

Graphs can be directed and undirected, their edges can form cycles. Sometimes a vertex
 can point to itself. Directed acyclic graph is often short-named "dags".

The number of outgoing edges a vertex has is called a vertex degree. Every finite
 undirected graph has an even number of vertices with odd degree. This is so called
 handshaking lemma, so named due to a notorious example. In a party of people some
 of whom shake hands, an even number of people must have shaken an odd number of
 other people's hands.

There are several ways to represent a graph. Most commonly used are adjacency list
 (array) and adjacency matrix (2D array) representations. This implementation uses
 vertex objects with adjacency list stored as an attribute of vertex.

Adjacency list can be used to represent both directed and undirected graph types.
 For an undirected graph, relation between adjacent vertices is always mutual, while
 in a directed graph, it is not necessarily the case.
"""


def dict_to_graph(D):
    """
    Converts dictionary into a set of graph and vertex objects

    Assumed dictionary representation is in following format:
     - `{'A': ['B', 'C']}` for unweighted graphs
     - `{'A': {'B': 3.0, 'C': 1.5}} for weighted graphs

    :param dict D: Input dictionary
    :return Graph: Output graph object
    """
    G = Graph()
    for k in D:
        v = Vertex(k)
        G.map[v.key] = v
        G.V.append(v)
    G.adj = D
    return G


class Graph:
    def __init__(self):
        """
        Basic adjacency list graph representation
        """
        self.V = []    # List of pointers to all vertices in a graph
        self.map = {}  # Map of pointers to all vertices in a graph by their key
        self.adj = {}  # Adjacency list graph representation

    def E(self):
        """
        Generates tuples of all edges in a graph

        :return __generator: Tuple of next edge in a graph
        """
        for u in self.map:
            for k in self.adj[u.key]:
                v = self.map[k]
                yield u, v

    def Adj(self, v):
        """
        Generates pointers to all adjacent vertices of a vertex

        :param Vertex v: Subject vertex
        :return __generator: Pointer to the next vertex
        """
        for k in self.adj[v.key]:
            yield self.map[k]


def degree(G, v):
    """
    Returns degree of a vertex (a number of outgoing edges)

    :param Graph G: Adjacency list representation of a graph
    :param Vertex v: Subject vertex
    :return int: Degree of a vertex
    """
    return len(G.adj[v.key])


def weight(G, u, v):
    """
    Returns weight of an edge `(u, v)`

    Assumes that edge is weighted.

    :param Graph G: Adjacency list representation of a weighted graph
    :param Vertex u: First vertex
    :param Vertex v: Second vertex
    :return float: Weight of an edge
    """
    e = G.adj[u.key]
    if type(e) is not dict:
        raise AttributeError("Not a weighted edge")
    return e[v.key]


class Vertex:
    def __init__(self, key):
        """
        Basic graph node

        Implementation of a basic graph node. Has useful attributes such as `color`
         and `p`, that are used for topological sort, depth-first and breadth-first
         search algorithms. Pointers to adjacent vertices are stored in a list `d`.

        :param Any key: Key (value) held by a vertex
        """
        self.key = key
        self.p = None  # Pointer to a parent vertex (from which it was visited)
        self.d = None  # Distance to the vertex from starting vertex (in BFS),
                       # ...time (counter) at which it was discovered (in DFS),
                       # ...shortest path estimate (in shortest path relaxation).
        self.f = None  # Time (counter) at which all adjacent vertices have been
                       # discovered (DFS has finished the vertex).
        self.color = None

    """
    Vertex comparison operators based on `d` value (used in edge prioritization)
    """

    def __lt__(self, other):
        return self.d < other.d

    def __le__(self, other):
        return self.d <= other.d

    def __gt__(self, other):
        return self.d > other.d

    def __ge__(self, other):
        return self.d >= other.d

    def __eq__(self, other):
        return self.d == other.d

    def __str__(self):
        return str(self.key)
