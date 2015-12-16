"""
This is the quickest implementation of Breadth First Search and Depth First Search
 that I could find. It uses dictionary representation of a graph. Although it can
 be easily rewritten to use Graph objects.
"""
graph = {'A': 'BF',
         'B': 'F',
         'C': 'DA',
         'D': 'E',
         'E': 'AB',
         'F': 'DC',
         }


def dfs(graph, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)  # first visit (topological sort)
    for next in graph[start]:  # first discovery (topological sort)
        if next not in visited:
            dfs(graph, next, visited)
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


def bfs(graph, start):
    visited, queue = [], [start]
    while queue:
        vertex = queue[0]
        del queue[0]
        if vertex not in visited:
            visited.append(vertex)
            queue.extend([v for v in graph[vertex] if v not in visited])
    return visited


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
