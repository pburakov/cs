"""
Topological Sort
================
"""
from basic.linked_list import LinkedList, Node as Node
from basic.linked_list import list_insert
from graphs import Graph, Vertex
from graphs.search import Counter, WHITE, GRAY, BLACK


def topological_sort(G):
    """Topological sort of a directed acyclic graph.

    Topological sort is a linear ordering of all vertices of a graph in order of precedence.
    If a graph :math:`G` contains an edge :math:`(u, v)` then :math:`u` appears before
    :math:`v` in the ordered set. If the graph contains a cycle, then no linear ordering is
    possible.

    Topological sort is a simple extension of a depth-first search algorithm. The code is
    almost identical to that of the DFS with the addition of the output linked list. An
    explored vertex is added to an output list.

    Complexity:
        :math:`O(V+E)` same as DFS, with :math:`O(V)` additional storage for the output list.

    :param Graph G: DAG.
    :return: List of vertices in order of precedence.

    """
    t = Counter()
    L = LinkedList()
    for u in G.V:
        u.color = WHITE
        u.p = None
    for u in G.V:
        if u.color is WHITE:
            visit(G, u, t, L)
    return L


"""
Subroutines used in topological sort
"""


def visit(G, u, t, L):
    """Vertex visit procedure for topological sort.

    The code is almost identical to the :func:`dfs_visit()` procedure with a simple addition
    of :func:`list_insert()`.

    Complexity:
        :math:`O(k)` where :math:`k` is number of adjacent vertices.

    :param Graph G: DAG.
    :param Vertex u: Vertex to visit.
    :param Counter t: Distance ticker.
    :param LinkedList L: Output list.

    """
    t.tick += 1
    u.d = t.tick
    u.color = GRAY
    for v in G.Adj(u):
        if v.color is WHITE:
            v.p = u
            visit(G, v, t, L)
    u.color = BLACK
    t.tick += 1
    u.f = t.tick
    list_insert(L, Node(u))  # Finished vertex is added onto the front of a linked list
