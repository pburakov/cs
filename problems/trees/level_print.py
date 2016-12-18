"""
# Tree Level Traversal

Implement an algorithm to print out nodes in a tree, level by level.

Example:
```
     a
    / \
   b   c
  / \   \
 d   e   f

Prints out:
a
b c
d e f
```
"""
from trees.binary import BinaryTreeNode as Node


def level_print(x):
    """
    Prints out binary tree nodes level by level.

    A tree is a linked data structure that can be regarded as a graph. Level by level
     tree traversal is performed using bread-first search-like algorithm. Level is
     printed out as soon as the frotnier had been discovered.

    Complexity: O(n)
    :param Node x: Starting node
    :return None: Prints to stdout
    """
    from queue import Queue
    Q = Queue()
    Q.put(x)
    nodes_on_curr_level = 1
    nodes_on_next_level = 0
    while not Q.empty():
        node = Q.get()
        print(str(node.key), end=' ')
        nodes_on_curr_level -= 1
        if node.left is not None:
            Q.put(node.left)
            nodes_on_next_level += 1
        if node.right is not None:
            Q.put(node.right)
            nodes_on_next_level += 1
        if nodes_on_curr_level == 0:
            nodes_on_curr_level = nodes_on_next_level
            nodes_on_next_level = 0
            print()  # Done with the level, starting next line
