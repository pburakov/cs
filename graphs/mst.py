"""
Minimum Spanning Trees
======================
"""

from heapq import heappush, heappop

from basic.disjoint_set import make_set, find_set, union
from graphs import Graph, Edge, Vertex, weight


def mst_kruskal(G):
    """Computes a minimum spanning tree of a graph.

    Complexity:
        :math:`O(E\\log V)`

    :param Graph G: Weighted graph.
    :return: List of edges.

    """
    A = []
    for v in G.V:
        make_set(v)
    E = []
    for u, v in G.E():  # Sort edges by their weight
        heappush(E, (weight(u, v), (u, v)))
    for _, (u, v) in E:
        if find_set(u) is not find_set(v):
            A.append(Edge(u, v))
            union(u, v)
    return A


def mst_prim(G, r):
    """Computes a minimum spanning tree of a graph.

    Complexity:
        :math:`O(V\\log V+E\\log V)`

    :param Graph G: Weighted graph.
    :param Vertex r: Root vertex.

    """
    for u in G.V:
        u.k = inf  # Using `k` as `key` is reserved
        u.p = None
    r.k = 0
    Q = []
    for v in G.V:  # Sort vertices by their `k` attribute
        heappush(Q, (v.k, v))
    while len(Q) > 0:
        _, u = heappop(Q)
        for v in G.Adj(u):
            if in_queue(v, Q) and weight(u, v) < v.k:
                v.p = u
                v.k = weight(u, v)


def in_queue(x, Q):
    """A utility function for Prim's algorithm that checks whether the vertex is in a queue.

    Complexity:
        :math:`O(n)` where :math:`n` is the number of tuples in the queue.

    :param Vertex x: Target vertex.
    :param list Q: Queue of tuples.
    :return: :data:`True` if vertex was found in a queue, :data:`False` otherwise.

    """
    for _, v in Q:
        if x == v:
            return True
    return False


inf = float("inf")
