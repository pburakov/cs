import unittest
from solutions.arrays.three_sum import *


class TestSolution(unittest.TestCase):
    def test(self):
        self.assertEqual(solution([1, -6, 3, 8, -2, 2]), [(-6, -2, 8)])
