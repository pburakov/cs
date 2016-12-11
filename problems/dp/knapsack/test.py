import unittest
from problems.dp.knapsack import *


class TestSolution(unittest.TestCase):
    def test(self):
        items = [
            Item(60, 5),
            Item(50, 3),
            Item(70, 4),
            Item(30, 2)
        ]
        self.assertEqual(backtrack(items, 5), 80)
        self.assertEqual(dp(items, 5), 80)
