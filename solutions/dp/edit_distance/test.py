import unittest
from solutions.dp.edit_distance import *


class TestSolution(unittest.TestCase):
    def test(self):
        self.assertEqual(backtrack("cats", "nut"), 3)
        self.assertEqual(dp("cats", "nut"), 3)
        self.assertEqual(backtrack("I like Python!", ""), 14)
        self.assertEqual(dp("I like Python!", ""), 14)
