"""
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

Complexity of all traversal algorithms is O(n), where `n` is the number of nodes
 in the tree (considering the function that is applied during traversal takes
 O(1)).
"""


def pre_order(x, f):
    """
    Pre-order tree traversal.

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

    :param Node x: Starting node
    :param (Node)->Any f: Procedure applied to a node on traversal
    :return None: Will apply function `f` to a traversed node
    """
    if x is not None:
        post_order(x.left, f)
        post_order(x.right, f)
        f(x)
