"""
Graph is a linked data structure represented by vertices and edges.

Some of the graph properties are ...

Types of edges are ...

Handshaking lemma is...

There are several ways to represent a graph. Most commonly used are adjacency list
 (array) and adjacency matrix (2D array) representations. This implementation uses
 vertex objects with adjacency list stored as an attribute of vertex.
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
        self.Adj = []  # List of pointers to adjacent vertices.
        self.p = None  # Pointer to a parent vertex (from which it was visited)
        self.d = None  # Distance to the vertex from parent node
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
        self.V = []  # Adjacency list of all vertices in a graph
