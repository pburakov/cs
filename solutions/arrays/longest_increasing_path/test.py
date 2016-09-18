import unittest
from solutions.arrays.longest_increasing_path import *


class TestSolution(unittest.TestCase):
    def test(self):
        m1 = [[3, 6, 7, 5],
              [2, 8, 9, 1],
              [4, 8, 10, 0],
              [6, 7, 3, 9]]
        cache = [[0 for _ in range(len(m1[0]))] for _ in range(len(m1))]
        self.assertEqual(longest_path(m1, 2, 3, cache), 1)
        self.assertEqual(longest_path(m1, 1, 3, cache), 2)
        self.assertEqual(longest_path(m1, 0, 3, cache), 3)
