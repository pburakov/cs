class Node:
    def __init__(self, v):
        self.v = v
        self.p = None
        self.rank = 0

    def __str__(self):
        return str(self.v)


def make_set(x):
    """Creates new set with a single element.

    :param basic.disjoint_set.Node x:

    """
    x.p = x
    x.rank = 0


def union(x, y):
    """

    :param basic.disjoint_set.Node x:
    :param basic.disjoint_set.Node y:

    """
    link(find_set(x), find_set(y))


def link(x, y):
    """Links roots of two disjoint sets.

    :param basic.disjoint_set.Node x:
    :param basic.disjoint_set.Node y:

    """
    if x.rank > y.rank:
        y.p = x
    else:
        x.p = y
        if x.rank == y.rank:
            y.rank = y.rank + 1


def find_set(x):
    """Finds the root of the element's set.

    :param basic.disjoint_set.Node x:
    :return: Root of the set.

    """
    if x != x.p:
        x.p = find_set(x.p)
    return x.p
