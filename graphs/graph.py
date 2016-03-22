class Node:
    """
    Implementation of basic Graph node. Has useful boolean properties such as
     `discovered` and `visited`, that can be used in Topological sort, Depth-
     First and Breadth-First Search algorithms.

    For example of DFS and BFS implementation, see /algorithms/bfs_dfs.py
    """

    def __init__(self, value):
        self.value = value
        self.connections = []
        self.discovered = False
        self.visited = False

    def __str__(self):
        return str(self.value)
