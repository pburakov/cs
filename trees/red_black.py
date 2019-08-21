"""
Red-Black Trees
===============

Red-Black tree is a "balanced" search-tree structure with one extra bit of storage per node: its **color**, which can either be RED or BLACK. By constraining the node colors on any simple path from the root to a leaf, red black trees ensure that no such path is more than twice as long as any other, so that the tree is approximately balanced.

A red-black tree is a binary tree that satisfies the following red black properties:

    1. Every node is either red or black.
    2. The root is black.
    3. Every leaf (null pointer) is black.
    4. If a node is red, the both its children are black.
    5. For each node, all simple paths from the node to descendant leaves contain the same number of black nodes.

The number of black nodes on any simple path from, but not including, a node :math:`x` down to a leaf is called the **black-height** of the node, denoted :math:`bh(x)`.
"""
from trees.bst import BST, Node as BSTNode
from trees.bst import left_rotate, right_rotate


class RedBlackTree(BST):
    """Red-Black Tree is an approximately balanced instance of a BST.
    """
    pass


class Node(BSTNode):
    """An augmented BST node with an additional color bit.
    """
    color = None

    def __init__(self, key):
        """An augmented BST node with an additional color bit.

        :param object key: Node's key.

        """
        super().__init__(key)


def rb_insert(T, z):
    """

    :param RedBlackTree T: Instance of Red-Black Tree to update.
    :param trees.red_black.Node z: Node to insert.
    :return:

    """
    y = None
    x = T.root
    while x is not None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y is None:
        T.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
    z.left = None
    z.right = None
    z.color = RED
    rb_insert_fixup(T, z)


def rb_insert_fixup(T, z):
    """

    :param RedBlackTree T:
    :param trees.red_black.Node z:

    """
    while z.p.color == RED:
        if z.p == z.p.p.left:
            y = z.p.p.right
            if y.color == RED:
                z.p.color = BLACK
                y.color = BLACK
                z.p.p.color = RED
                z = z.p.p
            elif z == z.p.right:
                z = z.p
                left_rotate(T, z)
            z.p.color = BLACK
            z.p.p.color = RED
            right_rotate(T, z.p.p)


# TODO

BLACK = "black"
RED = "red"
