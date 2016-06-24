"""
In a shortest path problem we are given a weighted directed graph. The weight
 of a path is the sum of weights of all of its constituent edges. Shortest path
 (defined by `∂(u, v)`) is defined by a minimum path weight, that is if a path
 `u -> v` exists, or by infinity otherwise. Note that edge weights can represent
 different metrics, not just the distance.

Shortest-path algorithms rely on the property that shortest path contains other
 shortest sub-paths within it. Some graphs may include edges whose weights are
 negative, so the shortest path in this graph would include more edges than its
 non-negative counterpart. Shortest path cannot contain a cycle, and some
 algorithms can detect and report their existence.

Shortest path is represented by a tree of vertex predecessors (as in breadth-
 first tree). Weight of a path to a vertex equals the sum of weights of all the
 edges that have led to the vertex.

Algorithms in this module cover solutions to single-source shortest path problem.
 They share technique of initialization, edge relaxation and shortest-path
 estimation.
"""

from graphs.graph import Graph, Vertex, weight


def initialize_single_source(G, s):
    """
    Initialization of shortest-path estimates and predecessor pointers

    Complexity: O(V).
    :param Graph G: Adjacency list graph representation
    :param Vertex s: Starting vertex
    :return None: Graph vertices are updated
    """
    for v in G.V():
        v.d = inf
        v.p = None
    s.d = 0


def relax(G, u, v):
    """
    Relaxes edge `(u, v)`

    Term "relaxation" actually means tightening an upper bound. The process
     consists of testing whether we can improve the shortest path to `v` found
     so far by going through `u` and if so, updating both the estimate and
     parent relation.

    Once upper bound property (minimum ∂) is achieved, it never changes. Relaxed
     edges also follow triangle inequality: `∂(s, v) ≤ ∂(s, u) + w(u, v)`.

    Complexity: O(1)
    :param Graph G: Adjacency list graph representation
    :param Vertex u: First vertex
    :param Vertex v: Second vertex
    :return None: Vertex `v` is updated
    """
    if v.d > u.d + weight(G, u, v):
        v.d = u.d + weight(G, u, v)
        v.p = u


def bellman_ford(G, s):
    """
    Bellman-Ford single-source shortest-paths solution in the general case

    Algorithm relaxes edges, making `|V|-1` passes over the edges of the graph,
     decreasing an estimate on the weight from starting vertex `s` to each vertex
     in a weighted directed graph. When cycle is done, it achieves the actual
     shortest-path weight ∂(s, v) on each edge.

    Second loop checks for cycles by verifying that triangle inequality has not
     been broken at least once.

    Complexity: O(VE) or O(V+VE+E). O(V) for initialization, O(E) for both loops.
    :param Graph G: Adjacency list weighted directed graph representation
    :param Vertex s: Starting vertex
    :return bool: Returns True iff the graph contains no negative-weight cycles
     that are reachable from the starting vertex, False otherwise.
    """
    n = len(G.v)  # Total number of vertices in a graph

    initialize_single_source(G, s)
    for i in range(0, n - 1):
        for u, v in G.E():
            relax(G, u, v)
    for u, v in G.E():
        if v.d > u.d + weight(G, u, v):
            return False
    return True


"""
Constants used in shortest paths
"""
inf = float("inf")
