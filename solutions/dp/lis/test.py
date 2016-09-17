import unittest
from solutions.dp.lis import *


class TestSolution(unittest.TestCase):
    def test(self):
        self.assertEqual(dp([1, 2, 3, 2, 1, 2, 3, 4, 1, 2]), [1, 2, 3, 4])
        self.assertEqual(dp([2, 4, 3, 5, 1, 7, 6, 9, 8, 6]), [2, 3, 5, 6, 8])
