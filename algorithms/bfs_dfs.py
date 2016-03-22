from graphs.graph import Node


def dfs(root, f):
    if not root.connections:
        return
    root.discovered = True
    f(root)
    root.visited = True
    for node in root.connections:
        node.discovered = True
        if node.visited is False:
            dfs(node, f)


def bfs(root, f):
    queue = []
    root.discovered = True
    queue.append(root)

    while queue:
        next = queue.pop(0)
        f(next)
        next.visited = True
        for n in next.connections:
            if n.discovered is False:
                n.discovered = True
                queue.append(n)


a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')
g = Node('G')
h = Node('H')

a.connections = [e, f]
b.connections = [f, d, g]
c.connections = [f, h]
d.connections = [b]
e.connections = [a]
f.connections = [a, b, c]
g.connections = [b]
h.connections = [c]

dfs(f, lambda x: print(x, end=' '))

# Nodes are mutable.
# Comment out dfs() before running bfs()
# bfs(f, lambda x: print(x, end=' '))
