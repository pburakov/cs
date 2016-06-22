from basic_data_structures.linked_list import LinkedList, Node, list_insert
from graphs.dfs import Timer, WHITE, GRAY, BLACK
from graphs.graph import Graph, Vertex


def topological_sort(G):
    """
    Topological sort of directed acyclic graph

    Topological sort is a linear ordering of all vertices of a graph in order of
     precedence. If graph `G` contains an edge `(u, v)` then `u` appears before `v` in
     the ordering. If the graph contains a cycle, then no linear ordering is possible.

    Topological sort is a simple extension of a depth-first search algorithm. The code
     is almost identical to that of the DFS with an addition of the output linked list.
     Vertex is inserted onto the front of an output list, once all of its edges have been
     explored and DFS "backtracked" to the vertex and its color has been changed to black,
     We can observe that the vertices in the output list would be arranged in reverse
     order of these events.

    Complexity: O(V+E) same as DFS, with O(V) additional storage for the output list
    :param Graph G: Adjacency list representation of a DAG
    :return LinkedList: List of vertices in order of precedence
    """
    t = Timer()
    L = LinkedList()

    for u in G.V:
        u.color = WHITE
        u.p = None
    for u in G.V:
        if u.color is WHITE:
            visit(u, t, L)
    return L


def visit(u, t, L):
    """
    Vertex visit procedure with topological sort

    Finished vertex is inserted at the head of linked list. The code is almost identical
     to the `dfs_visit()` procedure with a simple addition of `list_insert()`.

    Complexity: O(Adj) where `Adj` is number of adjacent vertices
    :param Vertex u: Vertex to visit
    :param Timer t: Mutable timer (integer counter)
    :param LinkedList L: Output linked list
    :return None: Finished vertex is updated and added to the list `L`
    """
    t.tick += 1
    u.d = t.tick
    u.color = GRAY
    for v in u.Adj():
        if v.color is WHITE:
            v.p = u
            visit(v, t, L)
    u.color = BLACK
    t.tick += 1
    u.f = t.tick
    list_insert(L, Node(u))  # Finished vertex is added onto the front of a linked list
