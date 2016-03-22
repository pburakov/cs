class Node:
    """
    Node of a binary tree
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


def pre_order(root, f):
    """
    Pre-order tree traversal. Function `f` is called on a visited node.
    """
    if root is not None:
        f(root)
        pre_order(root.left, f)
        pre_order(root.right, f)


def in_order(root, f):
    """
    In-order tree traversal. Function `f` is called on a visited node.
    """
    if root is not None:
        in_order(root.left, f)
        f(root)
        in_order(root.right, f)


def post_order(root, f):
    """
    Post-order tree traversal. Function `f` is called on a visited node.
    """
    if root is not None:
        post_order(root.left, f)
        post_order(root.right, f)
        f(root)
