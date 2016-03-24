from trees.binary_search_tree import Node
from trees.binary_search_tree import insert as bst_insert

"""
AVL tree Node implementation based on Binary Search Tree Node.
"""


def height(node):
    """
    Recursively calculates height (h) of a Node.

    :param Node node:
    :return int: calculated height of node
    """
    if node is None:
        return -1
    else:
        return max(height(node.left), height(node.right)) + 1


def balance(node):
    """
    Calculates balance factor (b) of a Node.

    :param Node node:
    :return int: For AVL trees -1 <= b <= 1
    """
    if node is None:
        return 0
    else:
        return height(node.left) - height(node.right)


def rotate_right(node):
    """
    Right tree rotation.

    :param Node node: current root Node of the rotation
    :return Node: new root Node after the rotation (pivot node)
    """
    new_root = node.left
    node.left = new_root.right
    if new_root.right:
        new_root.right.parent = node
    new_root.parent = node.parent
    if node.parent:
        # Is node left or right child?
        if node.parent.right is node:
            node.parent.right = new_root
        else:
            node.parent.left = new_root
    new_root.right = node
    node.parent = new_root
    return new_root


def rotate_left(node):
    """
    Left tree rotation.

    :param Node node: current root Node of the rotation
    :return Node: new root Node after the rotation (pivot node)
    """
    new_root = node.right
    node.right = new_root.left
    if new_root.left:
        new_root.left.parent = node
    new_root.parent = node.parent
    if node.parent:
        # Is node left or right child?
        if node.parent.right is node:
            node.parent.right = new_root
        else:
            node.parent.left = new_root
    new_root.left = node
    node.parent = new_root
    return new_root


def insert(node, root):
    """
    Same as BST insert but tree is automatically rebalanced after each insert,
     and a root of rebalanced tree is returned as it may shift.

    :param Node node: new Node
    :param Node root: root Node to start with
    :return Node: root node of a rebalanced tree
    """
    bst_insert(node, root)
    return rebalance(root)


def rebalance(node):
    """
    Rebalances the tree top-down starting at `node`.
    Returns the root of a rebalanced tree as it may shift

    :param Node node: root node to start rebalancing
    :return Node: root node of a rebalanced tree
    """
    balance_factor = balance(node)
    if balance_factor > 1:
        if balance(node.left) < 0:
            rotate_left(node.left)
        node = rotate_right(node)
    if balance_factor < -1:
        if balance(node.right) > 0:
            rotate_right(node.right)
        node = rotate_left(node)
    return node
