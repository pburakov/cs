import unittest
from solutions.linked_lists.two_sum import *


class TestSolution(unittest.TestCase):
    def test(self):
        l1 = List()
        l1.insert(Node(1))
        l1.insert(Node(2))
        l1.insert(Node(3))
        l1.insert(Node(1))
        l1.insert(Node(6))
        self.assertTrue(solution(l1, 5))
        self.assertTrue(solution(l1, 2))
        self.assertFalse(solution(l1, 1))
        self.assertFalse(solution(l1, 6))
