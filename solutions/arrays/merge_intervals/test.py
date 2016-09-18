import unittest
from solutions.arrays.merge_intervals import *


class TestSolution(unittest.TestCase):
    def test(self):
        i1 = [(1, 3), (3, 6), (1, 5), (2, 4), (7, 8)]
        self.assertEqual(solution(i1), [(1, 6), (7, 8)])
