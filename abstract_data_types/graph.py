class Graph:
    """
    Basic implementation of a Graph. Allows to add vertexes and edges as weighted
     directional connections between them.
    """

    def __init__(self):
        self.vertex_list = {}

    def add(self, key):
        new_vertex = Vertex(key)
        self.vertex_list[key] = new_vertex
        return new_vertex

    def connect(self, v1, v2, weight):
        if v1 not in self.vertex_list:
            self.add(v1)
        if v2 not in self.vertex_list:
            self.add(v2)
        self.vertex_list[v1].connect(self.vertex_list[v2], weight)


class Vertex:
    """
    Graph Vertex. Holds an id and a set of weighted connections.
    """

    def __init__(self, id):
        self.id = id
        self.connected_to = {}

    def connect(self, neighbour, weight=0):
        self.connected_to[neighbour] = weight

    def __str__(self):
        return str(self.id) + ' connected to: ' + str([n.id for n in self.connected_to])
