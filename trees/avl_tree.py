"""
AVL tree (Adelson-Velsky-Landis tree) is a height-based self-balancing binary
 search tree. It is an augmented BST that additionally keeps the height attribute
 of an individual node.

Besides regular BST properties, AVL tree keeps the heights of the two child subtrees
 of any node differ by at most one. Rebalancing is performed by one of more tree
 rotations on every update of a dynamic set. Balanced tree structure guarantees
 node lookup, insertion and deletion in O(log(n)) time.
"""
from trees.bst import tree_insert
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
        Augmented BST node with additional height attribute.

        :param Any key: Node's value (key)
        """
        super().__init__(key)
        self.height = 0


def height(x):
    """
    Returns height attribute of a node `x`.

    Null nodes (children of leaf nodes) have a height of -1 to make a height and
     balance factor formulae work. This algorithm assumes that height attributes of
     children nodes are correct.

    Complexity: O(1)
    :param Node x: Subject node
    :return int: Height of node `x`
    """
    if x is None:
        return -1
    else:
        return x.height


def update_height(x):
    """
    Calculates and writes height attribute into node `x`.

    This algorithm assumes that height attributes of children nodes are correct.

    Complexity: O(1).
    :param Node x: Subject node
    :return None: Node `x` is mutated in the process
    """
    x.height = max(height(x.left), height(x.right)) + 1


def balance_factor(x):
    """
    Returns balance factor of node `x`.

    This algorithm assumes that height attributes of children nodes are correct.

    Complexity: O(1).
    :param Node x: Subject node
    :return int: Balance factor of node `x`
    """
    return height(x.left) - height(x.right)


def avl_rebalance(T, x):
    """
    :param AVLTree T:
    :param Node x:
    :return:
    """
    while x is not None:
        pass


def avl_insert(T, z):
    """
    :param AVLTree T:
    :param Node z:
    :return None:
    """
    tree_insert(T, z)
    avl_rebalance(T, z)
