"""
If we parse mathematical expression  5 * 3 + 4 * 7 into a form of a tree:

    +
  *   *
 5 3 4 7

We can traverse this tree in-order to re-evaluate the expressions again.
Traversing this tree pre-order will generate same expression in Polish notation.

One way to improve this algorithm is using parentheses `(` and `)` using Stacks.
"""
from trees.binary_tree import Node
from trees.binary_tree import in_order
from trees.binary_tree import pre_order

root = Node('+')
root.left = Node('*')
root.left.left = Node(5)
root.left.right = Node(3)
root.right = Node('*')
root.right.left = Node(4)
root.right.right = Node(7)

in_order(root, lambda x: print(x, end=' '))
print()
pre_order(root, lambda x: print(x, end=' '))
