import unittest
from solutions.trees.lca import *


class TestSolution(unittest.TestCase):
    def test(self):
        root = a = Node('a')
        b = Node('b')
        c = Node('c')
        d = Node('d')
        e = Node('e')
        a.left = b
        a.right = c
        b.left = d
        b.right = e
        self.assertIs(find(root, b, c), a)
        self.assertIs(find(root, d, c), a)
        self.assertIs(find(root, d, e), b)
