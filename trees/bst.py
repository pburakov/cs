"""
Binary Search Tree
==================

BST (Binary Search Tree) is a convenient binary tree data structure that allows fast value
lookup. Basic operations on a complete BST take time proportional to a **height** of a
tree rather that the number of its elements.

The values (or **keys** as named in CLRS) in a BST are stored in such a way as to satisfy
the main BST property. For any **parent node** in a BST, its left child must hold a
smaller value and its right child must hold a bigger value.

Every node in a binary tree is a **root** to its own **subtree**. Inductively, BST
property guarantees that any value in a left subtree will be smaller than the root node
and any value in a right subtree will be bigger.

In-order printing of nodes in a BST will produce sorted output of its values. Nodes in
augmented BSTs can hold more properties and offer more efficient operations in a handful
of applications.

The correctness of these algorithms is guaranteed by the BST properties. Notice that the
update algorithms implemented here, such as :func:`tree_insert()`, :func:`transplant()`
and :func:`tree_delete()` (algorithms that cause the dynamic set represented by BST to
change) operate on an instance of BST, while query algorithms operate on arbitrary nodes.

Most BST operations take :math:`O(h)` time where *h* is a height of a tree. If tree is
perfectly complete and **balanced**, *h* will be *log(n)*. In worst case with all the
nodes on one side, BST will resemble a linked list and take *O(n)* as its height will be
proportional to the number of elements.
"""
from trees.binary import BinaryTree, BinaryTreeNode


class BinarySearchTree(BinaryTree):
    """Similar to a regular BinaryTree, holds a pointer to the root node.
    """
    pass


class BSTNode(BinaryTreeNode):
    """Augmented variant of a BinaryTreeNode with a pointer to its parent.
    """

    def __init__(self, key):
        """Augmented variant of a BinaryTreeNode with a pointer to its parent.

        :param object key: Node's key.

        """
        super().__init__(key)
        self.parent = None


def tree_search(x, k):
    """Recursive search query algorithm for finding a key in BST.

    Complexity:
        :math:`O(h)` where :math:`h` is the height of a tree.

    :param BSTNode x: Node to start the search with.
    :param object k: A key to search.
    :return: A found node or :data:`None` if key was not found in a tree.

    """
    if x is None or x.key == k:
        return x
    elif k < x.key:
        return tree_search(x.left, k)
    elif k > x.key:
        return tree_search(x.right, k)


def iterative_tree_search(x, k):
    """Iterative version of BST search algorithm.

    Iterative search is more efficient on most computers due to reduced use of a memory
    stack.

    Complexity:
        :math:`O(h)` where :math:`h` is the height of a tree.

    :param BSTNode x: Node to start the search with.
    :param object k: A key to search.
    :return: A found node or :data:`None` if key was not found in a tree.

    """
    while k is not None and k != x.key:
        if k < x.key:
            x = x.left
        elif k > x.key:
            x = x.right
    return x


def tree_minimum(x):
    """Returns a pointer to a node holding a minimum key.

    According to BST properties it is the leftmost node in a tree.

    Complexity:
        :math:`O(h)` where :math:`h` is the height of a tree.

    :param BSTNode x: Node to start the lookup.
    :return: Node holding minimum value.

    """
    while x.left is not None:
        x = x.left
    return x


def tree_maximum(x):
    """Returns a pointer to a node holding a maximum key.

    According to BST properties it is the rightmost node in a tree.

    Complexity:
        :math:`O(h)` where :math:`h` is the height of a tree.

    :param BSTNode x: Node to start the lookup.
    :return: Node holding maximum value.
    """
    while x.right is not None:
        x = x.right
    return x


def tree_successor(x):
    """Returns in-order successor of a node.

    Successor is a next node, determined by a sorted in-order tree traversal.

    Complexity:
        :math:`O(h)` where :math:`h` is the height of a tree.

    :param BSTNode x: Node to start the lookup.
    :return: Will return successor node if it exists, :data:`None` otherwise.

    """
    if x.right is not None:
        # Return minimum element (leftmost node) in a right subtree --
        return tree_minimum(x.right)
    else:
        # -- or, if there is no right child, go up the tree from `x` until
        # we encounter a node that is the left child of its parent.
        p = x.parent
        while p is not None and x is p.right:
            x = p
            p = p.parent
        return p


def tree_predecessor(x):
    """Returns in-order predecessor of a node.

    Predecessor is a previous node, determined by a sorted in-order tree traversal.

    Complexity:
        :math:`O(h)` where :math:`h` is the height of a tree.

    :param BSTNode x: Node to start the lookup.
    :return: Will return predecessor node if it exists, :data:`None` otherwise.

    """
    if x.left is not None:
        # Return maximum element (rightmost node) in a left subtree --
        return tree_maximum(x.left)
    else:
        # -- or, if there is no left child, go up the tree from `x` until
        # we encounter a node that is the right child of its parent
        p = x.parent
        while p is not None and x is p.left:
            x = p
            p = p.parent
        return p


def tree_insert(T, z):
    """Inserts a new node into BST.

    The node is inserted in such a way, that the properties of BST continue to hold. This
    algorithm is similar to `tree_search()` and can also be implemented recursively.

    Complexity:
        :math:`O(h)` where :math:`h` is the height of a tree, worst case :math:`\log n`.

    :param BinarySearchTree T: Instance of a BST to update.
    :param BSTNode z: New node, holding unique value (key).

    """
    p = None  # Pointer to a parent of a `z` node.
    q = T.root  # Node to start iteration with
    # Locate parent `p` to "attach" a new node to, while satisfying BST properties
    while q is not None:
        p = q  # Keep a trailing pointer to a parent
        if z.key == q.key:
            raise ValueError("Duplicate keys")
        elif z.key < q.key:
            q = q.left
        elif z.key > q.key:
            q = q.right
    z.parent = p  # `p` will remain None if new node is a root
    if p is None:
        T.root = z  # Tree was empty
    elif z.key < p.key:
        p.left = z
    elif z.key > p.key:
        p.right = z


def transplant(T, u, v):
    """Replaces one subtree as a child of its parent with another subtree.

    This simple utility method only helps moving subtrees around. It does not maintain BST
    properties, and does not update :math:`v` child sub-trees. It only maintains
    appropriate relations for parents of replaced nodes (if exists).

    Complexity:
        :math:`O(1)`.

    :param BinarySearchTree T: Instance of a BST to update.
    :param BSTNode u: Node to be replaced.
    :param BSTNode v: Node to replace :math:`u` with. Can be :data:`None`.

    """
    if u.parent is None:  # Node `u` is a root
        T.root = v
    elif u is u.parent.left:  # Node `u` is a left child of its parent
        u.parent.left = v
    else:  # Node `u` is a right child of its parent
        u.parent.right = v
    if v is not None:  # `u`'s parents become `v`'s parents
        v.parent = u.parent


def tree_delete(T, z):
    """Removes a node from a BST maintaining BST properties.

    This algorithm organizes its cases according to node location in a tree. These cases
    are described in detail in inline comments.

    Complexity:
        :math:`O(h)` where :math:`h` is the height of a tree, worst case :math:`\log n`.

    :param BinarySearchTree T: Instance of a BST to update.
    :param BSTNode z: Node to be deleted.

    """
    if z.left is None:  # `z` has only right child
        transplant(T, z, z.right)
    elif z.right is None:  # `z` has only left child
        transplant(T, z, z.left)
    else:  # `z` has both left and right child
        y = tree_minimum(z.right)  # `z`'s successor
        if y.parent is not z:  # Successor is not `z`'s right child
            transplant(T, y, y.right)
            y.right = z.right
            y.right.parent = y
        transplant(T, z, y)  # Successor is `z`'s right child
        y.left = z.left
        y.left.parent = y


def left_rotate(T, x):
    """Left rotation of a tree around pivot node.

    Rotation algorithm switches node pointers around so that the tree is rotated
    counter-clockwise around :math:`x`. Rotation is performed locally, assuming that
    :math:`x` has a right child.

    Order of operations is important so that no pointers are lost in the process. The
    method is accompanied by step-by-step inline comments to help remember these. In-order
    traversal of a tree should remain the same after rotation, thus proving that rotation
    did not damage BST properties.

    Complexity:
        :math:`O(1)`, only pointers are changed, other attributes of a node remain the same.

    :param BinarySearchTree T: Instance of a BST to update.
    :param BSTNode x: Node to pivot the tree around.

    """
    if x.right is None:
        raise ValueError("Node has no right child")
    y = x.right  # right subtree of `x`
    x.right = y.left
    if y.left is not None:
        y.left.parent = x
    y.parent = x.parent
    if x.parent is None:  # `x` was root
        T.root = y
    elif x is x.parent.left:  # `x` was a left child
        x.parent.left = y
    else:  # `x` was a right child
        x.parent.right = y
    y.left = x
    x.parent = y


def right_rotate(T, x):
    """Right rotation of a tree around pivot node.
    """
    if x.left is None:
        raise ValueError("Node has no left child")
    y = x.left  # left subtree of `x`
    x.left = y.right
    if y.right is not None:
        y.right.parent = x
    y.parent = x.parent
    if x.parent is None:
        T.root = y
    elif x is x.parent.right:
        x.parent.right = y
    else:
        x.parent.left = y
    y.right = x
    x.parent = y


def successor_order(x, f):
    """In-order traversal using iterative successor search algorithm.

    This algorithm has a small quirk. Although it might look like this algorithm runs in
    :math:`O(n \log n)` time, the amortized cost of this algorithm is the same as in-order
    traversal :math:`O(2n)` since every of :math:`n` edges of a BST is traversed exactly
    twice.

    Complexity:
        :math:`O(n)` amortized.

    :param BSTNode x: Starting node.
    :param (BSTNode)->Any f: Procedure called on node on traversal.

    """
    m = tree_minimum(x)
    f(m)
    y = tree_successor(m)
    while y is not None:
        f(y)
        y = tree_successor(y)
