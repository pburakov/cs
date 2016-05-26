"""
AVL tree (Adelson-Velsky-Landis tree) is a height-based self-balancing binary
 search tree. It is an augmented BST that additionally keeps the height attribute
 of an individual node.

Besides regular BST properties, AVL tree keeps the heights of the two child subtrees
 of any node differ by at most one. Rebalancing is performed by one of more tree
 rotations on every update of a dynamic set. Balanced tree structure guarantees
 node lookup, insertion and deletion in O(log(n)) time.
"""
from trees.bst import BST
from trees.bst import Node as BSTNode


class AVLTree(BST):
    """
    AVL tree is a self-balanced implementation of a BST
    """
    pass


class Node(BSTNode):
    def __init__(self, key):
        """
        Augmented BST node with additional height property

        :param Any key: Node's value (key)
        """
        super().__init__(key)
        self.height = 0


def height(x):
    """
    :param Node x:
    :return int:
    """
    if x is None:
        return -1
    else:
        return max(height(x.left), height(x.right)) + 1


def balance(x):
    """
    :param Node x:
    :return int:
    """
    return height(x.left) - height(x.right)
