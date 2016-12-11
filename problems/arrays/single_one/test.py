import unittest
from problems.arrays.single_one import *


class TestSolution(unittest.TestCase):
    def test(self):
        self.assertEqual(freq_map([1, 3, 2, 2, 1]), 3)
        self.assertEqual(binary([1, 3, 2, 2, 1]), 3)
