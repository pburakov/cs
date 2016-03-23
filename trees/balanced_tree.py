from trees.binary_search_tree import Node
from trees.binary_search_tree import *

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
    return height(node.left) - height(node.right)

#
# root = Node(2)
# insert(Node(7), root)
# insert(Node(9), root)
# insert(Node(5), root)
# insert(Node(1), root)
# insert(Node(3), root)
# insert(Node(4), root)
# insert(Node(6), root)
# insert(Node(8), root)
# print_tree(root)
# print("Root Height", height(root))
# print("Root Bal", balance(root))
