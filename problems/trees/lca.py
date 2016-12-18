"""
# Lowest Common Ancestor of Two Nodes

Find the lowest common ancestor (LCS) of two nodes in a binary tree (not necessarily
 a BST).

Example:
```
     a
    / \
   b   c
  / \
 d   e
LCA('e', 'd') -> 'b'
LCA('d', 'c') -> 'a'
```

You are given a pointer to a root of a tree two pointers to the target nodes. Your
 algorithm should not use parent pointers.
"""
from trees.binary import Node


def find(x, a, b):
    """
    Returns lowest common ancestor of two nodes in a binary tree.

    By definition and the properties of binary tree representation, the lowest common
     ancestor (LCA) is the first node which has both nodes `a` and `b` and different
     sub-trees. This is a top-down recursive algorithm that does not use a parent pointer.

    Complexity: O(n) where `n` is the number of nodes in a tree
    :param Node x: Starting node
    :param Node a: Pointer to the first node
    :param Node b: Pointer to the second node
    :return Optional[Node]: Lowest common ancestor of `a` and `b`, if it exists
    """
    if x is None:
        return None
    if x is a or x is b:
        return x
    in_l = find(x.left, a, b)
    in_r = find(x.right, a, b)
    if in_l and in_r:
        return x
    else:
        return in_l or in_r
