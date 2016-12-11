import unittest
from problems.graphs.count_islands import *


class TestSolution(unittest.TestCase):
    def test(self):
        m1 = [
            [0, 0, 0, 1, 1],
            [1, 1, 0, 0, 1],
            [0, 1, 0, 1, 1],
            [0, 0, 0, 0, 1],
            [0, 0, 1, 0, 0]
        ]
        self.assertEqual(solution(m1), 3)
