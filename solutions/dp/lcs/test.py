import unittest
from solutions.dp.lcs import *


class TestSolution(unittest.TestCase):
    def test(self):
        self.assertEqual(backtrack("BABCA", "ABCBA"), "ABC")
        self.assertEqual(dp("BABCA", "ABCBA"), "ABC")
