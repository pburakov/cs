import unittest
from problems.linked_lists.clone_list import *


class TestSolution(unittest.TestCase):
    def test(self):
        l1 = List()
        a = Node('a')
        b = Node('b')
        c = Node('c')
        d = Node('d')
        e = Node('e')
        e.other = c
        d.other = a
        l1.insert(e)
        l1.insert(d)
        l1.insert(c)
        l1.insert(b)
        l1.insert(a)
        l2 = clone(l1)
        self.assertEqual(str(l1), str(l2))
