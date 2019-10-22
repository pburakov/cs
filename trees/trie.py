"""
Suffix Tree
===========
"""


class Node:
    def __init__(self, key):
        self.key = key
        self.c = {}  # Children nodes
        self.terminal = False  # Denotes if node is a terminal node


class Trie:

    def __init__(self):
        self.root = Node(None)


def insert(T, W):
    """Inserts a word into a Trie

    :param Trie T: Suffix tree.
    :param str W: Word to insert.

    """
    node = T.root
    for i in range(len(W)):
        if W[i] not in node.c:
            node.c[W[i]] = Node(W[i])
        node = node.c[W[i]]
    node.terminal = True


def prefix(T, p):
    """Returns if there is any word in the trie that starts with the given prefix.

    :param Trie T: Suffix tree.
    :param str p: Target prefix.
    :rtype: Node
    """
    node = T.root
    for i in range(len(p)):
        if p[i] in node.c:
            node = node.c[p[i]]
        else:
            return None
    return node


def search(T, W):
    """Returns true if the word is in the trie, false otherwise.

    :param Trie T: Suffix tree.
    :param str W: Target word.
    :rtype: bool

    """
    node = prefix(T, W)
    if node is not None:
        return node.terminal
    else:
        return False
