import unittest
from problems.arrays.three_sum import *


class TestSolution(unittest.TestCase):
    def test(self):
        self.assertEqual(solution([1, -6, 3, 8, -2, 2]), [(-6, -2, 8)])
        self.assertEqual(solution([-7, 6, 2, 1, -3, 1, 5]), [(-7, 1, 6), (-7, 2, 5), (-3, 1, 2)])
