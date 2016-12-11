import unittest
from basic_data_structures.linked_list import LinkedList as List
from basic_data_structures.linked_list import list_insert
from problems.linked_lists.delete_duplicates import *


class TestSolution(unittest.TestCase):
    def test(self):
        l1 = List()
        list_insert(l1, Node(1))
        list_insert(l1, Node(2))
        list_insert(l1, Node(2))
        list_insert(l1, Node(3))
        list_insert(l1, Node(4))
        list_insert(l1, Node(4))
        list_insert(l1, Node(4))
        solution(l1.head)
        node = l1.head
        for i in range(4, 0, -1):
            self.assertEqual(node.key, i)
            node = node.next
