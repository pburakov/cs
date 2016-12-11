import unittest
from problems.linked_lists.cycle import *


class TestSolution(unittest.TestCase):
    def test(self):
        ll = LinkedList()
        a = Node('a')
        b = Node('b')
        c = Node('c')
        d = Node('d')
        e = Node('e')
        ll.head = a
        a.next = b
        b.next = c
        c.next = d
        d.next = e
        e.next = b
        self.assertIs(find(ll), b)
        e.next = e
        self.assertIs(find(ll), e)
        a.next = a
        self.assertIs(find(ll), a)
