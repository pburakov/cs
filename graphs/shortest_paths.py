"""
In a shortest path problem we are given a **weighted directed graph**. The weight of a
 path is the sum of weights of all of its constituent edges. Shortest path (defined by
 *∂(u, v)*) is defined by a minimum path weight, that is if a path *u -> v* exists, or by
 infinity otherwise. Note that edge weights can represent different metrics, not just the
 distance.

Shortest-paths algorithms rely on the property that shortest path contains other shortest
 sub-paths within it. Some graphs may include edges whose weights are negative, so the
 shortest path in this graph would include more edges than its non-negative counterpart.
 Shortest path cannot contain a cycle, and some algorithms can detect and report their
 existence.

Shortest path is represented by a tree of vertex predecessors (as in breadth-first tree).
 Weight of a path to a vertex equals the sum of weights of all the edges that have led to
 the vertex. Vertex predecessor is another vertex with which it shares the most relaxed
 edge. If we follow parent records in a predecessor-tree all the way to the starting
 vertex after search was finished, we'll get the shortest route it would take to reach
 the destination vertex.

Algorithms in this module cover solutions to **single-source shortest paths** problem.
 They share the technique of initialization, edge relaxation and shortest-path estimation.
 Other powerful method worth mentioning is a *bidirectional search* (not implemented
 here). Longest path can be calculated by negating weights.
"""
from graphs import Graph, Vertex, weight


def dag_shortest_paths(G, s):
    """
    Generic shortest-paths algorithm for dags.

    The algorithm starts by topologically sorting the dag. If the dag contains a
     shortest path from vertex `u` to vertex `v`, then `u` precedes `v` in the
     topological sort. We can make just one pass over the vertices in sorted order.

    The concept of continuous relaxation, assuming that the shortest path to a
     previous  vertex already has already been solved to optimality, is commonly
     used in dynamic programming.

    Complexity: O(V+E) linear size in the size of adjacency list representation.
     Topological sort takes O(V+E) time, O(V) for initialization, O(E) for
     relaxation, as each edge is relaxed exactly once (aggregated analysis).
    :param Graph G: Adjacency list weighted dag representation
    :param Vertex s: Starting vertex
    :return None: Graph vertices are updated
    """
    from graphs.topological_sort import topological_sort

    L = topological_sort(G)
    initialize_single_source(G, s)
    for node in L:
        u = node.key  # Gets vertex from a linked list
        for v in G.Adj(u):
            relax(u, v)


def bellman_ford(G, s):
    """
    Bellman-Ford single-source shortest-paths solution in the general case.

    Algorithm relaxes edges, making `|V|-1` passes over the edges of the graph,
     decreasing an estimate on the path from starting vertex `s`, gradually spreading
     the frontier of relaxed edges beyond those already estimated. In that sense,
     Bellman-Ford is also commonly regarded as a dynamic programming algorithm.

    After `|V|-1` passes of every edge in a graph, it will deterministically
     completely relax all of its edges, unless there's a negative-weight cycle.
     Second loop checks for cycles by verifying that none of the edges can be
     further relaxed otherwise reporting that negative-weight cycle exists.

    Complexity: O(VE) for main loop. Initialization O(V) + O(E) for cycle check.
    :param Graph G: Adjacency list weighted directed graph representation
    :param Vertex s: Starting vertex
    :return bool: Returns True iff the graph contains no negative-weight cycles
     that are reachable from the starting vertex, False otherwise. Graph vertices
     are updated.
    """
    n = len(G.V)  # Total number of vertices in a graph
    initialize_single_source(G, s)
    for i in range(0, n - 1):
        # Relax every edge `|V|-1` times
        for u, v in G.E():
            relax(u, v)
    for u, v in G.E():
        # Check if edge cannot be further relaxed
        if v.d > u.d + weight(u, v):
            return False
    return True


def dijkstra(G, s):
    """
    Dijkstra single-source shortest-paths algorithm.

    In contrast to Bellman-Ford, Dijkstra's algorithm uses greedy strategy on solving
     the single-source shortest paths problems for the case in which all edge weights in
     a DAG are non-negative. It is very similar to BFS, only it prioritises "lightest"
     edges with the smallest estimate (hence the strategy name).

    Greedy approach does not always yield optimal results, but Dijkstra algorithm does
     indeed compute shortest paths. Each time vertex `u` is added to the set `S`, `u.d`
     is already `∂(s, u)` (completely relaxed).

    Dijkstra algorithm is easy to modify to make it solve single-source single-target
     problem. All we need is to stop the while loop once the target vertex is found.

    This implementation uses min-priority queue built with the list vertices keyed by
     their `d` values. Priority queue is built after initialization, but it also needs
     to be rebuilt after series of edge relaxations.

    Complexity: O(E log V) (or O(EV) with this implementation of min-heap). There are at
     most |reachable E| relax operations. If we manage to maintain heap properties after
     each relaxation it is possible to keep extract min operation at `log V` time.
     O(V lg V + E) running time is achievable with a Fibonacci heap.
    :param Graph G: Adjacency list representation of a weighted directed graph with
     non-negative weights.
    :param Vertex s: Starting vertex
    :return None: Graph vertices are updated
    """
    from basic_data_structures.heaps import build_min_heap, min_heap_extract

    initialize_single_source(G, s)
    S = []  # Set of vertices whose final shortest-path weights have been determined
    Q = G.V
    while len(Q) > 0:
        build_min_heap(Q)  # Weights might have been updated after relaxation
        u = min_heap_extract(Q, False)  # Heap rebuilding is skipped
        S.append(u)
        for v in G.Adj(u):
            relax(u, v)
    G.V = S  # Optional step to maintain Graph object


"""
Constants and subroutines used in shortest paths algorithms
"""
inf = float("inf")


def path_string(G, s, v):
    """
    Returns vertices on a shortest path between two vertices as a string.

    This procedure assumes search/path has already computed the predecessor tree.

    :param Graph G: Adjacency list graph representation
    :param Vertex s: Starting vertex
    :param Vertex v: Finishing vertex
    :return str: Output string
    """
    if v is s:
        return str(s)
    elif v.p is None:
        raise RecursionError("No such path is found")
    else:
        return path_string(G, s, v.p) + ' ' + str(v)


def initialize_single_source(G, s):
    """
    Initialization of shortest-path estimates and predecessor pointers.

    Complexity: O(V).
    :param Graph G: Adjacency list graph representation
    :param Vertex s: Starting vertex
    :return None: Graph vertices are updated
    """
    for v in G.V:
        v.d = inf
        v.p = None
    s.d = 0


def relax(u, v):
    """
    Relaxes edge (u, v).

    Term "relaxation" actually means tightening an upper bound. The process
     consists of testing whether we can improve the shortest path to `v` found
     so far by going through `u` and if so, updating both the estimate and
     parent relation.

    Once upper bound property (∂) is achieved, it never changes. Relaxed edges
     also follow triangle inequality: `∂(s, v) ≤ ∂(s, u) + w(u, v)`.

    Longest path can be calculated using negated weights.

    Complexity: O(1)
    :param Vertex u: Source vertex
    :param Vertex v: Target vertex
    :return None: Vertex `v` is updated
    """
    w = weight(u, v)
    if v.d > u.d + w:
        v.d = u.d + w
        v.p = u
