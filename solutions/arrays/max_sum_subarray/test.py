import unittest
from solutions.arrays.max_sum_subarray import *


class TestSolution(unittest.TestCase):
    def test(self):
        l1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.assertEqual(max_sum(l1), 6)
        self.assertEqual(subarray(l1), [4, -1, 2, 1])
