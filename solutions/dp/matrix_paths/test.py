import unittest
from solutions.dp.matrix_paths import *


class TestSolution(unittest.TestCase):
    def test(self):
        m0 = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(backtrack(m0), 10)
        m1 = [
            [0, 0, 1],
            [0, 0, 0],
            [1, 0, 0]
        ]
        self.assertEqual(backtrack(m1), 4)
        m2 = [
            [0, 1, 0],
            [0, 0, 0],
            [1, 1, 0]
        ]
        self.assertEqual(backtrack(m2), 1)
