"""
This is the quickest implementation of Breadth First Search and Depth First Search
 that I could find. It uses dictionary representation of a graph. Although it can
 be easily rewritten to use Graph objects.

Breadth-first search (BFS) and depth first-search (DFS) are actually the same, apart
 from the data structure used to store discovered vertices hence affecting the order
 in which they are discovered.

A BFS keeps a queue of vertices that have been discovered and are yet to be visited,
 and then repeatedly visits the front vertex on the queue, discovering all of its
 neighbours and adding those to the back of the queue. This means that the earlier
 a vertex is discovered, the earlier it is visited, giving the 'breadth-first'
 shape of the search.

A DFS simply replaces the queue of the BFS with a stack, so that newly discovered
 vertices are visited right away, and vertices discovered longer ago are only
 returned to once the new vertices have been visited. This causes the search to
 'dive' right to the end of the first search path before considering any other
 vertices.

It's worth mentioning that DFS algorithm is used in topological sort (see comments in
 `dfs()` method.

So BFS and DFS are actually the same algorithm, parametrised by the internal data
  structure."""

graph = {'A': 'BF',
         'B': 'F',
         'C': 'DA',
         'D': 'E',
         'E': 'AB',
         'F': 'DC',
         }


def dfs(graph, start, visited=None):
    # List is a mutable type in Python so can't add default value visited=[]
    # to the function arguments
    if visited is None:
        visited = []
    visited.append(start)  # first visit (use for topological sort)
    for next in graph[start]:  # first discovery (use for topological sort)
        if next not in visited:
            # Immediately going deeper
            dfs(graph, next, visited)
    return visited


def bfs(graph, start):
    visited, queue = [], [start]
    while queue:
        vertex = queue[0]
        del queue[0]
        if vertex not in visited:
            visited.append(vertex)
            # Adding all discovered vertices to the queue
            queue.extend([v for v in graph[vertex] if v not in visited])
    return visited


def dfs_paths(graph, start, goal, path=None):
    """
    Generator
    """
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next in graph[start]:
        if next not in path:
            yield from dfs_paths(graph, next, goal, path + [next])


def bfs_paths(graph, start, goal):
    """
    Generator
    """
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue[0]
        del queue[0]
        for next in graph[vertex]:
            if next not in path:
                if next == goal:
                    yield path + [next]
                else:
                    queue.append((next, path + [next]))


def path_exists(graph, start, goal):
    for path in dfs_paths(graph, start, goal):
        if len(path) > 1:
            return True
    return False


print('DFS:', dfs(graph, 'A'))
print('BFS:', bfs(graph, 'A'))
print(list(bfs_paths(graph, 'A', 'E')))
print(list(dfs_paths(graph, 'A', 'E')))
