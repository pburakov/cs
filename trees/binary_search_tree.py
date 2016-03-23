from trees.binary_tree import Node as BinaryTreeNode


class Node(BinaryTreeNode):
    """
    Same as a Node of a regular tree but keeps a reference to its parent for
     faster Node replacement. Each Node of a tree is a root of a subtree tree.
    """

    def __init__(self, value):
        super().__init__(value)
        self.parent = None

    """
     Comparison operators overloading. Compare Node values.
    """

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value


def search(node, root):
    """
    Recursive search algorithm for a Binary Search Tree

    :param Node node: new Node
    :param Node root: root Node to start with
    :return: Node|None
    """
    if root is None:
        return None
    if node == root:
        return root
    elif node < root:
        return search(node, root.left)
    elif node > root:
        return search(node, root.right)


def insert(node, root):
    """
    Recursive insert algorithm for a Binary Search Tree

    :param Node node: new Node
    :param Node root: root Node to start with
    :return: None
    """
    if node == root:
        raise ValueError("Duplicate values")
    elif node < root:
        if root.left is not None:
            insert(node, root.left)
        else:
            node.parent = root
            root.left = node
    elif node > root:
        if root.right is not None:
            insert(node, root.right)
        else:
            node.parent = root
            root.right = node


def find_min(root):
    """
    Recursive search algorithm for a Node holding a minimum value in a
     Binary Search Tree

    :param Node root: root Node to start searching from
    :return: Node
    """
    if root.left is None:
        return root
    else:
        return find_min(root.left)


def find_successor(node):
    """
    Returns next in-order successor for the node. Lookup is based on BST properties.

    :param Node node: Node to look up successor for
    :return Node|None
    """
    if node is None:
        return None
    if node.right:
        return find_min(node.right)
    elif node.parent:
        return node.parent
    else:
        return None


def replace(node, new_node):
    """
    Replaces the Node while maintaining references to adjacent Nodes.

    :param Node node: old Node
    :param Node new_node: new Node
    :return: new Node with references to children and parents taken from
     old Node.
    """
    if node.parent is not None:
        parent = node.parent
        # Is left child?
        if parent.left and parent.left == node:
            parent.left = new_node
        # Is right child?
        elif parent.right and parent.right == node:
            parent.right = new_node
        # Orphaned node?
        else:
            raise KeyError("Incorrect parent-children relation")
    if node.left:
        new_node.left = node.left
        new_node.left.parent = new_node
    if node.right:
        new_node.right = node.right
        new_node.right.parent = new_node
    return new_node


def print_tree(root):
    """
    An MIT.edu string implementation of Binary Search Tree
    """
    if root is None: return '<empty tree>'

    def recurse(node):
        if node is None: return [], 0, 0
        label = '(' + str(node.value) + ')'
        left_lines, left_pos, left_width = recurse(node.left)
        right_lines, right_pos, right_width = recurse(node.right)
        middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
        pos = left_pos + middle // 2
        width = left_pos + middle + right_width - right_pos
        while len(left_lines) < len(right_lines):
            left_lines.append(' ' * left_width)
        while len(right_lines) < len(left_lines):
            right_lines.append(' ' * right_width)
        if (middle - len(label)) % 2 == 1 and node.parent is not None and \
                        node is node.parent.left and len(label) < middle:
            label += '.'
        label = label.center(middle, '.')
        if label[0] == '.': label = ' ' + label[1:]
        if label[-1] == '.': label = label[:-1] + ' '
        lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                 ' ' * left_pos + '/' + ' ' * (middle - 2) +
                 '\\' + ' ' * (right_width - right_pos)] + \
                [left_line + ' ' * (width - left_width - right_width) +
                 right_line
                 for left_line, right_line in zip(left_lines, right_lines)]
        return lines, pos, width

    print('\n'.join(recurse(root)[0]))
