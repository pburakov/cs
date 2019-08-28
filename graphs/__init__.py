"""
Graph Representation
====================

Graph is a linked data structure comprised of **vertices** (nodes or points) and **edges**
(lines, arrows or arcs) representing relationships between vertices.

Graphs can be directed and undirected, and their edges can form cycles. Sometimes a vertex
can point to itself. **Directed acyclic graph** is often short-named DAG.

The number of outgoing edges a vertex has is called a vertex **degree**. Every finite
undirected graph has an even number of vertices with an odd degree. This property is called
a *handshaking lemma*, so named due to a notorious example. In a party of people some of
whom shake hands, an even number of people must have shaken an odd number of other
people's hands.

There are several ways to represent a graph. Most commonly used are **adjacency list**
and **adjacency matrix** (2D array).

Adjacency list can be used to represent both directed and **undirected graph** types. For
an undirected graph, relation between adjacent vertices is always mutual, while in a
directed graph, it is not necessarily the case.
"""


class Graph:
    """Basic adjacency list graph representation.

    This implementation uses a hash-map to store vertices.
    """

    def __init__(self):
        """Basic adjacency list graph representation.
        """
        self.map = {}  # Map of vertices, keyed by their key
        self.V = []  # Vertices as list

    def Adj(self, v):
        """Iterates through adjacent vertices of a vertex.

        :param Vertex v: Source vertex.
        :return: Next adjacent vertex in an arbitrary order.

        """
        v = self.map[v.key]
        for k in v.f_edges:
            yield self.map[k]

    def E(self):
        """Iterates through all edges in a graph as tuples of vertices.

        :return: Next tuple of vertices in an arbitrary order.

        """
        for i in self.map:
            u = self.map[i]
            for j in u.f_edges:
                v = self.map[j]
                yield u, v


class Edge:
    """Edge of a graph.

    Points to source vertex, target vertex and has an optional weight value.
    """

    def __init__(self, u, v, w=None):
        """Edge of a graph.

        :param Vertex u: Source vertex.
        :param Vertex v: Target vertex.
        :param float w: (optional) Weight of an edge.

        """
        self.u = u
        self.v = v
        self.weight = w


def degree(v):
    """Returns degree of a vertex.

    Degree of a vertex is the number of edges that are incident to the vertex.

    :param Vertex v: Subject vertex.
    :return: Degree of a vertex.

    """
    return len(v.f_edges)


def potential(x):
    """Returns a potential of a vertex.

    Potential value :math:`p>0` changes weights of incident edges. Potential introduces a
    heuristic that helps to reduce the running time by ordering adjacent edges in a
    goal-directed search, thus allowing to hit the search target sooner.

    :param Vertex x: Subject vertex.
    :return: Potential of a vertex.

    """
    return x.pt


def weight(u, v):
    """Returns weight of an edge.

    Assumes that edge :math:`(u, v)` is weighted. Note that weights can be affected by a
    vertex potential. In searching algorithms, the priority is given to the edges with
    the lowest or the highest weight.

    :param Vertex u: Source vertex.
    :param Vertex v: Adjacent target vertex.
    :return: Weight of an edge.

    """
    E = u.f_edges[v.key]
    if E.weight is None:
        raise AttributeError("Not a weighted edge")
    return E.weight - potential(u) + potential(v)


class Vertex:
    """Basic graph node with attributes.
    """

    def __init__(self, k):
        """Basic graph node with attributes.

        :param object k: Key held by a vertex

        """
        self.key = k

        self.d = None
        # Depending on a running algorithm, `d` represents one of the following:
        #  - in BFS - distance to this vertex from a starting vertex;
        #  - in DFS - the time (counter) at which it was discovered;
        #  - in shortest-paths - :math:`(s, v)` path-weight estimate after edge relaxation.

        self.f = None  # The time (counter) at which DFS has finished the vertex.
        self.color = None  # Denotes vertex discovery status.
        self.p = None  # Pointer to a parent :data:`Vertex` (from which it was visited).
        self.pt = 0.0  # Potential modifier of a vertex.
        self.f_edges = {}  # Forward edges keyed by destination vertex key
        self.r_edges = {}  # Reverse (incoming) edges keyed by source vertex key

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


def dict_to_graph(D):
    """Converts dictionary into a graph.

    Utility function. Assumed dictionary representation is in following format:
     - ``{'A': ['B', 'C']}`` for unweighted graphs
     - ``{'A': {'B': 3.0, 'C': 1.5}}`` for weighted graphs

    Please note, that hash map (:data:`dict`) data type does not guarantee order
    preservation, which may lead to random results in certain algorithms, such as DFS.

    :param dict D: Input dictionary.
    :return: Output :data:`Graph` object.

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


class Counter:
    """Simple mutable ticker.
    """
    tick = 0

    def __init__(self, t=0):
        """Simple mutable ticker.

        :param int t: Starting number.

        """
        self.tick = t
