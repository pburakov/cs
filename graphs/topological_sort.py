"""
Topological Sort
================
"""
from basic_data_structures.linked_list import LinkedList, Node, list_insert
from graphs import Graph, Vertex
from graphs.search import Counter, WHITE, GRAY, BLACK


def topological_sort(G):
    """Topological sort of directed acyclic graph.

    Topological sort is a linear ordering of all vertices of a graph in order of precedence.
    If graph :math:`G` contains an edge :math:`(u, v)` then :math:`u` appears before
    :math:`v` in the ordering. If the graph contains a cycle, then no linear ordering is
    possible.

    Topological sort is a simple extension of a depth-first search algorithm. The code is
    almost identical to that of the DFS with an addition of the output linked list. Vertex
    is inserted onto the front of an output list. Once all of its edges have been explored
    and DFS "backtracked" to the vertex and its color has been changed to `black`, we can
    observe that the vertices in the output list would be arranged in reverse order of
    these events.

    Complexity:
        :math:`O(V+E)` same as DFS, with :math:`O(V)` additional storage for the output list.

    :param Graph G: Adjacency list representation of a DAG.
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

    Finished vertex is inserted at the head of linked list. The code is almost identical to
    the :func:`dfs_visit()` procedure with a simple addition of :func:`list_insert()`.

    Complexity:
        :math:`O(Adj)` where :math:`Adj` is number of adjacent vertices.

    :param Graph G: Adjacency list representation of a DAG.
    :param Vertex u: Vertex to visit.
    :param Counter t: Mutable timer (integer counter).
    :param LinkedList L: Output linked list.

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
