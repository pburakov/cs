import unittest
from solutions.trees.build import *
from trees.binary.traversal import in_order


class TestSolution(unittest.TestCase):
    def test(self):
        a = [i for i in range(1, 10)]
        b = []
        root = build_tree(a)
        in_order(root, lambda x: b.append(x.key))
        self.assertEqual(a, b)
