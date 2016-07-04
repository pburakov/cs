"""
Binary Tree is a linked data structure, where each node can point to two other
 nodes at most. These nodes are called left and right child nodes. Nodes that don't
 have any children pointers (replaced with `None`) are called leafs.

Every node in a binary tree is a root to its own subtree. This property allows the
 implementation of easy to understand recursive traversal algorithms that operate
 within a subtree of arbitrary node (not necessarily the root of a whole tree).

Traversal algorithms are called pre-order, post-order and in-order, so named because
 of the sequence in which the algorithm "visits" a node between the traversal of its
 left and right subtree without mutating the node (for example printing its value on
 the screen). This operation recurs until all the nodes in a sub-tree are eventually
 "visited".

Such operations that don't change the dynamic set of a tree are called querying.
 Operations that cause change are called updating.
"""


class BinaryTree:
    def __init__(self):
        """
        Binary Tree set representation class that holds a pointer to its root.
        """
        self.root = None


class Node:
    def __init__(self, key):
        """
        Node of a binary tree.

        Holds a value of any type (called a key) and pointers to left and/or right
         child.

        :param object key: Node's value (key)
        """
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key)


def pre_order(x, f):
    """
    Pre-order tree traversal.

    Complexity: O(n) where `n` is the number of nodes in the tree and `f` is O(1)
    :param Node x: Starting node
    :param (Node)->Any f: Procedure applied to a node on traversal
    :return None: Will apply function `f` to a traversed node
    """
    if x is not None:
        f(x)
        pre_order(x.left, f)
        pre_order(x.right, f)


def in_order(x, f):
    """
    In-order tree traversal.

    Complexity: O(n) where `n` is the number of nodes in the tree and `f` is O(1)
    :param Node x: Starting node
    :param (Node)->Any f: Procedure applied to a node on traversal
    :return None: Will apply function `f` to a traversed node
    """
    if x is not None:
        in_order(x.left, f)
        f(x)
        in_order(x.right, f)


def post_order(x, f):
    """
    Post-order tree traversal.

    Complexity: O(n) where `n` is the number of nodes in the tree and `f` is O(1)
    :param Node x: Starting node
    :param (Node)->Any f: Procedure applied to a node on traversal
    :return None: Will apply function `f` to a traversed node
    """
    if x is not None:
        post_order(x.left, f)
        post_order(x.right, f)
        f(x)
