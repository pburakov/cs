"""
Single Source Shortest Paths
============================

In a shortest path problem we are given a **weighted directed graph**. The weight of a
path is the sum of weights of all of its constituent edges. The shortest path :math:`\delta
(u,v)` is defined by a minimum path weight, that is if a path :math:`u\\to v` exists, and
by infinity otherwise. Note that edge weights can represent different metrics, not just
the distance. Longest path can be calculated by negating weights.

Shortest-paths algorithms rely on the property stating that the shortest path contains
other shortest sub-paths within it. A graph may include edges with negtive weights, so the
shortest path in such graph would include more edges than its non-negative counterpart.
Shortest path cannot contain a cycle, and some algorithms can detect and report their
existence.

Shortest path is represented by a tree of vertex predecessors (as in breadth-first tree).
Weight of a path to a vertex equals the sum of weights of all the edges which led to the
vertex. In a shortest-path traversal, a vertex predecessor is an adjacent vertex with which
it shares the most relaxed edge. Inductively, if we follow parent records in a
predecessor-tree all the way to the starting vertex once the search was finished, we'll get
the shortest route it would take to reach the destination vertex.

Algorithms in this module cover solutions to a **single-source shortest paths** problem.
They share the steps of initialization, edge relaxation and shortest-path estimation.
Other powerful method worth mentioning is a *bidirectional search*.
"""
from basic.heaps import build_min_heap, min_heap_extract
from graphs import Graph, Vertex, weight
from graphs.topological_sort import topological_sort


def dag_shortest_paths(G, s):
    """Generic shortest-paths algorithm for DAGs.

    The algorithm starts by topologically sorting the DAG. If the DAG contains a shortest
    path from vertex :math:`u` to vertex :math:`v`, then :math:`u` precedes :math:`v` in
    the topologically sorted set. Once the set is sorted, we can make just one pass over
    the vertices to calculate completely relaxed edges.

    The concept of continuous relaxation, assuming that the shortest path to a previous
    vertex already has already been solved to optimality, is commonly used in dynamic
    programming.

    Complexity:
        :math:`O(V+E)` linear to the size of adjacency list representation. Topological
        sort takes :math:`O(V+E)` time, :math:`O(V)` for initialization, :math:`O(E)` for
        relaxation. Each edge is relaxed exactly once (aggregated analysis).

    :param Graph G: Weighted DAG.
    :param Vertex s: Starting vertex.

    """
    L = topological_sort(G)
    initialize_single_source(G, s)
    for node in L:
        u = node.key  # Gets vertex from a linked list
        for v in G.Adj(u):
            relax(u, v)


def bellman_ford(G, s):
    """Bellman-Ford single-source shortest-paths solution in the general case.

    Algorithm relaxes edges by making :math:`|V|-1` passes over the edges of the graph,
    decreasing an estimate on the path from starting vertex :math:`s`, gradually spreading
    the frontier of relaxed edges beyond those already estimated. In that sense,
    Bellman-Ford is also commonly regarded as the first dynamic programming algorithm.

    After :math:`|V|-1` passes, the algorithm will deterministically relax all of its
    edges, unless there's a negative-weight cycle. The second loop checks for cycles
    by verifying that none of the edges can be further relaxed.

    Complexity:
        :math:`O(VE)` for main loop. Initialization and cycle check are :math:`O(V) + O(E)`.

    :param Graph G: Weighted directed graph.
    :param Vertex s: Starting vertex.
    :return: :data:`True` iff the graph contains no negative-weight cycles that are
     reachable from the starting vertex, :data:`False` otherwise.

    """
    n = len(G.V)  # Total number of vertices in a graph
    initialize_single_source(G, s)
    for i in range(0, n - 1):
        # Relax every edge `|V|-1` times
        for u, v in G.E():
            relax(u, v)
    for u, v in G.E():
        # Check if an edge cannot be further relaxed
        if v.d > u.d + weight(u, v):
            return False
    return True


def dijkstra(G, s):
    """Dijkstra single-source shortest-paths algorithm.

    In contrast to Bellman-Ford, Dijkstra's algorithm uses greedy strategy on solving the
    single-source shortest paths problem for the case in which all edge weights in a DAG
    are non-negative. Dijkstra's algortithm is basically a BFS with a heurisitc. The
    algorithm prioritises the "lightest" edges with a smallest estimate.

    Greedy approach does not always yield optimal results, but Dijkstra algorithm does
    indeed compute shortest paths. Each time a vertex :math:`u` is added to the set
    :math:`S`, :math:`u.d` attribute is already :math:`\delta (s,u)` (completely relaxed).

    Dijkstra algorithm is easy to modify to solve a single-source single-target problem.
    We only need to stop the loop once the target vertex is found.

    This implementation uses a priority queue (min-heap) to sort the vertices by their
    :math:`d` values.

    Complexity:
        :math:`O(E \log V)`. There are at most :math:`|\\textrm{reachable } E|` relax
        operations. If we manage to maintain heap properties after each relaxation it is
        possible to keep :func:`min_heap_extract()` operation at :math:`\log V` time.
        :math:`O(V\lg V+E)` running time is achievable with a Fibonacci heap.

    :param Graph G: Weighted directed graph with non-negative weights.
    :param Vertex s: Starting vertex.

    """
    initialize_single_source(G, s)
    S = []  # Set of vertices whose final shortest-path weights have been determined
    Q = G.V
    while len(Q) > 0:
        build_min_heap(Q)  # Weights might have been updated after relaxation
        u = min_heap_extract(Q)
        S.append(u)
        for v in G.Adj(u):
            relax(u, v)
    G.V = S  # Optional step to update Graph object


"""
Constants and subroutines used in shortest paths algorithms
"""
inf = float("inf")


def path_string(G, s, v):
    """Prints out the shortest path between two vertices in a graph.

    This procedure assumes search/path has already computed the predecessor tree.

    :param Graph G: A graph with calculated shortest paths.
    :param Vertex s: Source vertex.
    :param Vertex v: Target vertex.
    :return: Output string.

    """
    if v is s:
        return str(s)
    elif v.p is None:
        raise RecursionError("No such path is found")
    else:
        return path_string(G, s, v.p) + ' ' + str(v)


def initialize_single_source(G, s):
    """Initialization of shortest-path estimates and predecessors.

    Complexity:
        :math:`O(V)`.

    :param Graph G: A graph.
    :param Vertex s: Starting vertex.

    """
    for v in G.V:
        v.d = inf
        v.p = None
    s.d = 0


def relax(u, v):
    """Relaxes a graph edge.

    Term "relaxation" actually means tightening an upper bound. The process consists of
    testing whether we can improve the shortest path to :math:`v` found so far by going
    through :math:`u` and if so, updating both the estimate and parent relation.

    Once upper bound property :math:`\delta` is achieved, it never changes. Relaxed edges
    also follow the triangle inequality: :math:`\delta (s, v) ≤ \delta (s, u) + w(u, v)`.

    Complexity:
        :math:`O(1)`.

    :param Vertex u: Source vertex.
    :param Vertex v: Adjacent target vertex.

    """
    w = weight(u, v)
    if v.d > u.d + w:
        v.d = u.d + w
        v.p = u
