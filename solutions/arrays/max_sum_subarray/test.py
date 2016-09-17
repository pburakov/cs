import unittest
from solutions.arrays.max_sum_subarray import *


class TestSolution(unittest.TestCase):
    def test(self):
        a1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        a2 = [0, 1, -1, 2, -2, 4, -3]
        a3 = [10, -4, 3, 2, -10]
        a4 = [0]
        a5 = [-2, -4, 2, -1, 1, -3]
        self.assertEqual(max_sum(a1), 6)
        self.assertEqual(subarray(a1), [4, -1, 2, 1])
        self.assertEqual(max_sum(a2), 4)
        self.assertEqual(subarray(a2), [4])
        self.assertEqual(max_sum(a3), 11)
        self.assertEqual(subarray(a3), [10, -4, 3, 2])
        self.assertEqual(max_sum(a4), 0)
        self.assertEqual(subarray(a4), [0])
        self.assertEqual(max_sum(a5), 2)
        self.assertEqual(subarray(a5), [2, -1, 1])
