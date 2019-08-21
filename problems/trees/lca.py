"""
Lowest Common Ancestor of Two Nodes
===================================

Find the lowest common ancestor (LCS) of two nodes in a binary tree (not necessarily a
BST). You are given a pointer to a root of a tree two pointers to the target nodes.
Algorithm should not use parent pointers.
"""
from trees.binary import Node as Node


def find(x, a, b):
    """Returns lowest common ancestor of two nodes in a binary tree.

    By definition and the properties of binary tree representation, the lowest common
    ancestor (LCA) is the first node which has both nodes :math:`a` and :math:`b` in
    different sub-trees. This is a top-down recursive algorithm that does not use a parent
    pointer.

    This algorithm assumes that both nodes :math:`a` and :math:`b` are present in the tree,
    however it can be updated to support an edge case when one or no target nodes are not
    in the tree. For example, we increment a counter every time a target node (or both) is
    found. If after the traversal the counter is anything but :math:`2`, then one (or both)
    of the target nodes is missing.

    Complexity:
        :math:`O(n)` where :math:`n` is the number of nodes in a tree.

    :param Node x: Starting node.
    :param Node a: Pointer to the first target node.
    :param Node b: Pointer to the second target node.
    :return: Lowest common ancestor of two nodes, if it exists.

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
