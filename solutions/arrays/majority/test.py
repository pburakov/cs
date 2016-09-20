import unittest
from solutions.arrays.majority import *


class TestSolution(unittest.TestCase):
    def test(self):
        self.assertEqual(find([7, 2, 7]), 7)
        self.assertEqual(find([1, 2, 3, 2]), 2)
        self.assertEqual(find([9, 2, 3, 2, 4, 5]), None)
