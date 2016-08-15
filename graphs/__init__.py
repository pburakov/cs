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
 vertex and edge objects with a combination of adjacency maps.

Adjacency list can be used to represent both directed and undirected graph types.
 For an undirected graph, relation between adjacent vertices is always mutual, while
 in a directed graph, it is not necessarily the case.
"""


def dict_to_graph(D):
    """
    Converts dictionary into a graph and set of vertex and edge objects.

    Assumed dictionary representation is in following format:
     - `{'A': ['B', 'C']}` for unweighted graphs
     - `{'A': {'B': 3.0, 'C': 1.5}} for weighted graphs

    Please note, that hash map (dict) data type does not guarantee order preservation,
     which may lead to random results in certain algorithms, such as DFS.

    :param dict D: Input dictionary
    :return Graph: Output graph object
    """
    G = Graph()
    for i in D:  # Creating pointers for all vertices
        v = Vertex(i)
        G.map[v.key] = v
        G.V.append(v)
    for i in D:  # Creating edges
        u = G.map[i]
        for j in D[i]:
            if type(D[i]) is dict:
                w = D[i][j]  # Weighted graph
            else:
                w = None
            v = G.map[j]
            u.f_edges[j] = Edge(u, v, w)
            v.r_edges[i] = Edge(v, u, w)
    return G


class Graph:
    def __init__(self):
        """
        Basic adjacency list graph representation.
        """
        self.map = {}  # Map of pointers to all vertices, keyed by their key
        self.V = []  # List of pointers to all vertices, keyed by their key

    def Adj(self, v):
        """
        Generates pointers to all adjacent vertices of a vertex.

        :param Vertex v: Subject vertex
        :return __generator: Pointer to the next vertex
        """
        v = self.map[v.key]
        for k in v.f_edges:
            yield self.map[k]

    def E(self):
        """
        Generates all edges in a graph.

        :return __generator[Edge]: Next edge in a graph
        """
        for i in self.map:
            u = self.map[i]
            for edge in u.f_edges:
                assert isinstance(edge, Edge)
                yield edge


class Edge:
    def __init__(self, u, v, w=None):
        """
        Edge of a graph object representation.

        :param Vertex u: Source vertex
        :param Vertex v: Target vertex
        :param float w: (optional) Weight of an edge
        """
        self.u = u
        self.v = v
        self.weight = w


def degree(v):
    """
    Returns degree of a vertex (a number of outgoing edges).

    :param Vertex v: Subject vertex
    :return int: Degree of a vertex
    """
    return len(v.f_edges)


def potential(v):
    """
    Returns a potential of a vertex.

    :param Vertex v: Subject vertex
    :return float: Potential of a vertex
    """
    return v.pt


def weight(e):
    """
    Returns weight of an edge (u, v).

    Assumes that edge is weighted. Note that weights can be affected by a potential
     function, reducing the running time by prioritizing edges in a goal-directed
     search, thus allowing to hit the search target sooner.

    :param Edge e: Subject edge
    :return float: Weight of an edge
    """
    if e.weight is None:
        raise AttributeError("Not a weighted edge")
    return e.weight - potential(e.u) + potential(e.v)


class Vertex:
    def __init__(self, k):
        """
        Basic graph node.

        :param object k: Key (or label) held by a vertex
        """
        self.key = k
        self.f_edges = {}  # Forward edges keyed by destination vertex key
        self.r_edges = {}  # Reverse (incoming) edges keyed by source vertex key

        """
        Depending on a running algorithm, value `d` represents different attributes
        of a vertex:
         - in BFS - distance to the vertex from a starting vertex
         - in DFS - time (counter) at which it was discovered
         - in shortest-paths - `(s, v)` path-weight estimate after edge relaxation
        """
        self.d = None

        self.f = None  # Time (counter) at which DFS has finished the vertex
        self.color = None  # Used to denote vertex discovery status
        self.p = None  # Pointer to a parent vertex (from which it was visited)
        self.pt = 0.0  # Potential of a vertex (used in reduced edge cost estimation)

    """
    Vertex comparison operators based on `d` value (used in Dijkstra edge prioritization)
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
