import unittest
from solutions.dp.cut_rod import *


class TestSolution(unittest.TestCase):
    def test(self):
        p = [0, 1, 5, 8, 9]
        self.assertEqual(backtrack(p, 4), 10.0)
        self.assertEqual(backtrack(p, 3), 8.0)
        self.assertEqual(backtrack(p, 2), 5.0)
        self.assertEqual(memoized(p, 4), 10.0)
        self.assertEqual(memoized(p, 3), 8.0)
        self.assertEqual(memoized(p, 2), 5.0)
        self.assertEqual(dp(p, 4), 10.0)
        self.assertEqual(dp(p, 3), 8.0)
        self.assertEqual(dp(p, 2), 5.0)
