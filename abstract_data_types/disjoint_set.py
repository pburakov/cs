"""
This is a basic implementation of a Disjoint Set with Union Find algorithm.
 The code is nearly a copy of a pseudocode in this great Wikipedia article:
 https://en.wikipedia.org/wiki/Disjoint-set_data_structure

Methods:
 MakeSet(x) - initializes disjoint set for object x
 Find(x) - returns representative object of the set containing x
 Union(x,y) - makes two sets containing x and y respectively into one set with
  the use of path compression.
"""


def make_set(x):
    x.parent = x
    x.rank = 0


def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root.rank > y_root.rank:
        y_root.parent = x_root
    elif x_root.rank < y_root.rank:
        x_root.parent = y_root
    elif x_root != y_root:
        y_root.parent = x_root
        x_root.rank += 1


def find(x):
    if x.parent == x:
        return x
    else:
        x.parent = find(x.parent)
        return x.parent


class Node:
    """
    Node class is a implementation of a single Disjoint Set element that holds a
    single property label with a string representation of it.
    """

    def __init__(self, label):
        self.label = label

    def __str__(self):
        return str(self.label)


n = 7
set = [Node(ch) for ch in range(0, n)]
print("objects labels:\t\t\t", [str(i) for i in set])

[make_set(node) for node in set]
union(set[1], set[4])
print('joined 1 and 4')
union(set[1], set[2])
print('joined 1 and 2')
union(set[4], set[3])
print('joined 4 and 3')
sets = [str(find(x)) for x in set]
print("set representatives:\t", sets)
print('2 found with', find(set[2]))
print('1 found with', find(set[1]))
print('3 found with', find(set[3]))
print('5 found with', find(set[5]))
