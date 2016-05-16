"""
Binary Tree is a linked data structure, where each node can point to two other
 nodes at most. These nodes are called left and right child nodes.

Most well-known type of a binary tree is called BST (Binary Search Tree) (see
 trees/bst.py).

Every node in a binary tree is a root to its own subtree. This property allows the
 implementation of easy to understand recursive traversal algorithms.

Traversal algorithms are called in-order, pre-order and post-order, so named because
 of the sequence in which the algorithm "visit" a node (for example prints
 its value or possibly mutates traversed node) between the traversal of its left and
 right subtree. This operation recurs until all the nodes in a tree are eventually
 "visited".

Complexity of all traversal algorithms is O(n), where `n` is the number of nodes
 in the tree (considering the function that is applied during traversal takes
 O(1)).
"""


class Node:
    """
    Node of a binary tree. Holds a value of any type (called a key) and pointers
     to left and right child.
    """

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key)


def pre_order(root, f):
    """
    Pre-order tree traversal.

    :param Node root: Starting node
    :param callable f: Callback function
    :return None: Will call function `f` on every node traversal
    """
    if root is not None:
        f(root)
        pre_order(root.left, f)
        pre_order(root.right, f)


def in_order(root, f):
    """
    In-order tree traversal.

    :param Node root: Starting node
    :param callable f: Callback function
    :return None: Will call function `f` on every node traversal
    """
    if root is not None:
        in_order(root.left, f)
        f(root)
        in_order(root.right, f)


def post_order(root, f):
    """
    Post-order tree traversal.

    :param Node root: Starting node
    :param callable f: Callback function
    :return None: Will call function `f` on every node traversal
    """
    if root is not None:
        post_order(root.left, f)
        post_order(root.right, f)
        f(root)
