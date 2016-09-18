import unittest
from solutions.combinatorial.symbolic_parens import *


class TestSolution(unittest.TestCase):
    def test(self):
        self.assertEqual(count_ways("1|0", False), 0)
        self.assertEqual(count_ways("1&0", False), 1)
        self.assertEqual(count_ways("1^0|0|1", False), 2)
        self.assertEqual(count_ways("0&0&0&1^1|0", True), 10)
        self.assertEqual(count_ways("0&0&0&1^1|0", False), 32)
