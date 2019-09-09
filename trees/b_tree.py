"""
B-Tree
======

"""

t = 2  # Minimum degree of a B-Tree


class BTree:
    """A tree data structure in which each node has a large number of children.
    """

    def __init__(self):
        """A tree data structure in which each node has a large number of children.
        """
        self.root = None


class Node:
    """Node of a B-tree.

    Every node of a B-tree contains attributes such as the total number of stored keys
    :math:`n`, the keys themselves, stored in nondecreasing order, and a boolean value
    determining whether node :math:`x` is a leaf node or an internal node. Internal node
    also contains :math:`n+1` pointers to its children.

    """

    def __init__(self):
        self.n = 0  # Number of keys currently stored in the node
        self.key = [None] * (2 * t - 1)  # List of keys themselves
        self.leaf = False  # Denotes if the node is a leaf node
        self.c = [None] * 2 * t  # Children nodes


def b_tree_search(x, k):
    """Searches subtree starting at a given node to find the target key.

    Searching B-tree is much like searching a binary tree, except that instead of making a
    binary branding decision at each node, we make a multiway branching decision according
    to the number of the node's children.

    Complexity:
        :math:`O(th)=O(t\\log_t n)`, where :math:`h` is the height of the B-tree and
        :math:`n` is the number of keys in the B-tree. The procedure accesses
        :math:`O(h)=O(\\log_t n)` disk pages and spends :math:`O(t)` time on key scanning
        at each node.

    :param trees.b_tree.Node x: Root node.
    :param object k: Target key.
    :return: A tuple containing a pointer to the target node and the index of a target key
     or :data:`None` if a key was not found in a tree.

    """
    i = 0
    while i < x.n and k > x.key[i]:
        i += 1
    if i < x.n and k == x.key[i]:
        return x, i
    if x.leaf:
        return None
    else:
        # disk_read(x.c[i])
        return b_tree_search(x.c[i], k)


def b_tree_create(T):
    """Creates an empty root node in a given B-Tree.

    Complexity:
        :math:`O(1)` CPU time and :math:`O(1)` disk operations.

    :param BTree T: B-Tree instance.

    """
    x = Node()
    x.leaf = True
    x.n = 0
    # disk_write(x)
    T.root = x


def b_tree_split_child(x, i):
    """Splits the child node of a given root node at a given index.

    The procedure splits the child :math:`y=x.c_i` in two and adjusts the parent node
    :math:`x` so that it has an additional child :math:`z`. The child :math:`y` is split
    about its median key which is moved to the parent node :math:`x`. The new child
    :math:`z` then inherits :math:`t` largest children and :math:`t-1` keys above the
    median key of :math:`y`, and :math:`y`'s key count is reduced. The tree thus grows in
    height by one.

    After the split operation, a node might end up containing unused "leftover" keys
    beyond :math:`n`.

    Complexity:
        :math:`\\theta(t)`. The procedure performs :math:`O(1)` disk operations.

    :param trees.b_tree.Node x: Nonfull internal node which is a parent of the node being
     split.
    :param int i: Index of a full child node.

    """
    z = Node()
    y = x.c[i]  # The child to split
    z.leaf = y.leaf
    # `z` takes the largest `t-1` keys and corresponding `t` children of `y`
    z.n = t - 1
    for j in range(0, t - 1):
        z.key[j] = y.key[j + t]
    if not y.leaf:
        for j in range(0, t):
            z.c[j] = y.c[j + t]
    y.n = t - 1  # Adjust the key count for `y`
    for j in range(x.n, i, -1):
        x.c[j + 1] = x.c[j]  # Shift `x`'s children to the right
    x.c[i + 1] = z  # `z` becomes a new child of `x`
    for j in range(x.n - 1, i - 1, -1):
        x.key[j + 1] = x.key[j]  # Shift `x`'s keys to the right
    x.key[i] = y.key[t - 1]  # Move the median key to `x`
    x.n = x.n + 1
    # disk_write(y)
    # disk_write(z)
    # disk_write(x)


def b_tree_insert(T, k):
    """Inserts a key into a B-Tree.

    The procedure uses :func:`b_tree_split_child()` to guarantee that the recursion never
    descents to a full node.

    Complexity:
        :math:`O(th)=O(t\\log_t n)`, where :math:`h` is the height of the B-tree and
        :math:`n` is the number of keys in the B-tree. The procedure takes a single pass
        down the tree requiring :math:`O(h)` disk accesses.

    :param BTree T: B-Tree instance.
    :param object k: New key.

    """
    r = T.root
    if r.n == 2 * t - 1:
        s = Node()
        T.root = s
        s.leaf = False
        s.n = 0
        s.c[0] = r
        b_tree_split_child(s, 0)
        b_tree_insert_nonfull(s, k)
    else:
        b_tree_insert_nonfull(r, k)


def b_tree_insert_nonfull(x, k):
    """Inserts a key into a nonfull node of B-Tree.

    The case in which :math:`x` is a leaf is trivial. We simply write a new key to its
    appropriate location. If :math:`x` is not a leaf node, then we must insert :math:`k`
    into the appropriate leaf node in the subtree rooted at internal node :math:`x`.

    Complexity:
        :math:`O(th)=O(t\\log_t n)`. The number of pages that need to be in memory at any
        time is :math:`O(1)`.

    :param trees.b_tree.Node x: Nonfull node.
    :param object k: New key.

    """
    i = x.n - 1
    if x.leaf:
        while i >= 0 and k < x.key[i]:
            x.key[i + 1] = x.key[i]  # Shift keys to the right
            i -= 1
        x.key[i + 1] = k
        x.n += 1
        # disk_write(x)
    else:
        # Find the child to which the recursion would descend
        while i >= 0 and k < x.key[i]:
            i -= 1
        i += 1
        # disk_read(x.c[i])
        if x.c[i].n == 2 * t - 1:  # The child is full
            b_tree_split_child(x, i)
            # Find which of the two children is now the correct one to descend to
            if k > x.key[i]:
                i += 1
        b_tree_insert_nonfull(x.c[i], k)
