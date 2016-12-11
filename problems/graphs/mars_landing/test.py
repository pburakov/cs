import unittest
from problems.graphs.mars_landing import *


class TestSolution(unittest.TestCase):
    def test(self):
        p = [(0, 0), (0, 3), (3, 1)]
        m = [
            ['-', 'x', 'x', '-'],
            ['-', '-', 'x', '-'],
            ['-', '-', '-', '-'],
            ['-', '-', '-', '-'],
        ]
        self.assertEqual(find_landing(m, p), (2, 1))
