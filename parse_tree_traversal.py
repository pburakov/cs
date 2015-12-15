from abstract_data_types.stack import Stack
from trees.binary_tree import BinaryTree


def expression_to_tree(string):
    """
    This parser converts mathematical expression as a string into a Binary Tree
     by stacking the Nodes whenever mathematical operators '+', '-', '/', '*',
     '(' and ')' as they are encountered.

    Parsing rules:
     1. If the current token is a '(', add a new node as the left child of the
      current node, and descend to the left child.
     2. If the current token is in the list ['+','-','/','*'], set the root value
      of the current node to the operator represented by the current token. Add a
      new node as the right child of the current node and descend to the right child.
     3. If the current token is a number, set the root value of the current node
      to the number and return to the parent.
     4. If the current token is a ')', go to the parent of the current node.

    Note: requires usage of both parentheses and whitespaces for correct
     expression validation.

    Example inputs:
     wrong: (10 + 3) * 5
     right: ( ( 10 + 3 ) * 5 )
    """
    expression = string.split()
    stack = Stack()
    tree = BinaryTree('')
    stack.add(tree)
    for i in expression:
        if i == '(':
            tree.insert_left('')
            stack.add(tree)
            tree = tree.left_child
        elif i not in '+-*/)':
            tree.value = int(i)
            parent = stack.pop()
            tree = parent
        elif i in '+-*/':
            tree.value = i
            tree.insert_right('')
            stack.add(tree)
            tree = tree.right_child
        elif i == ')':
            tree = stack.pop()
        else:
            raise ValueError
    return tree


def pre_order(tree):
    """
    Traverses the Tree recursively and prints out the nodes in pre-order notation.
    """
    if tree:
        print(tree.value, end=' ')
        pre_order(tree.left_child)
        pre_order(tree.right_child)


def post_order(tree):
    """
    Traverses the Tree recursively and prints out the nodes in post-order notation.
    """
    if tree:
        post_order(tree.left_child)
        post_order(tree.right_child)
        print(tree.value, end=' ')


def in_order(tree):
    """
    Traverses the Tree recursively and prints out the nodes in in-order notation.
    """
    if tree:
        in_order(tree.left_child)
        print(tree.value, end=' ')
        in_order(tree.right_child)


def exp(tree):
    """
    Writes a mathematical expression based on an parse tree. Extends the
     case of in-order Tree Traversal with added parentheses. Node containing
     an operator is expected to have both left and right Children.
    """
    output = ""
    close_brackets = False
    if tree:
        if tree.left_child and tree.right_child:
            close_brackets = True
            output += '('
        output += exp(tree.left_child)
        output += str(tree.value)
        output += exp(tree.right_child)
        if close_brackets:
            output += ')'
    return output


expression = "( ( 1 + 2 ) * ( 3 + 4 ) )"
print('expression', expression)
tree = expression_to_tree(expression)

print('\npost order:')
post_order(tree)
print('\npre order:')
pre_order(tree)
print('\nin order:')
in_order(tree)
print('\nprint exp:')
print(exp(tree))
