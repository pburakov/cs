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
