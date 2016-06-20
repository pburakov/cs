"""
Graph is a linked data structure comprised of vertices (nodes or points) and edges
 (lines, arrows or arcs) representing relationships between vertices.

Graphs can be directed and undirected, their edges can form cycles, sometimes a vertex
 can point to itself. Directed acyclic graph are often short-named "dags".

Every finite undirected graph has an even number of vertices with odd degree. This
 is so called handshaking lemma, so named due to a notorious example. In a party of
 people some of whom shake hands, an even number of people must have shaken an odd
 number of other people's hands.

There are several ways to represent a graph. Most commonly used are adjacency list
 (array) and adjacency matrix (2D array) representations. This implementation uses
 vertex objects with adjacency list stored as an attribute of vertex.

Adjacency list can be used to represent both directed and undirected graph types.
 For an undirected graph, relation between adjacent vertices is always mutual, while
 in a directed graph, it is not necessarily the case.
"""


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
        self.Adj = []  # Adjacency list for the vertex. Can be used to represent
                       # ...both directed and undirected graph types.
        self.p = None  # Pointer to a parent vertex (from which it was visited)
        self.d = None  # Distance to the vertex from starting vertex (in BFS)
                       # ...or time (counter) at which it was discovered (in DFS).
        self.f = None  # Time (ticker) at which all adjacent vertices have been
                       # discovered (DFS has finished the vertex).
        self.color = None

    def degree(self):
        """
        Returns degree of a vertex (a number of adjacent vertices)

        :return int: Degree of a vertex
        """
        return len(self.Adj)

    def __str__(self):
        return str(self.key)


class Graph:
    def __init__(self):
        """
        Basic graph adjacency list graph representation
        """
        self.V = []  # List of all vertices in a graph
