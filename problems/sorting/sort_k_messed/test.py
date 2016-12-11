import unittest
from problems.sorting.sort_k_messed import *


class TestSolution(unittest.TestCase):
    def test(self):
        a = [3, 1, 2, 5, 4, 7, 6]
        sort(a, 2)
        self.assertEqual(a, [1, 2, 3, 4, 5, 6, 7])
