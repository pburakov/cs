import unittest
from problems.sorting.merge_in_place import *


class TestSolution(unittest.TestCase):
    def test(self):
        a = [1, 250, 600]
        b = [100, 200, 300, 0, 0, 0]
        sort(a, b)
        self.assertEqual(b, [1, 100, 200, 250, 300, 600])
