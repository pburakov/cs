import unittest
from basic_data_structures.linked_list import Node
from basic_data_structures.linked_list import list_insert
from problems.linked_lists.two_sum import *


class TestSolution(unittest.TestCase):
    def test(self):
        l1 = List()
        list_insert(l1, Node(1))
        list_insert(l1, Node(2))
        list_insert(l1, Node(3))
        list_insert(l1, Node(1))
        list_insert(l1, Node(6))
        self.assertTrue(solution(l1, 5))
        self.assertTrue(solution(l1, 2))
        self.assertFalse(solution(l1, 1))
        self.assertFalse(solution(l1, 6))
