import unittest
from solutions.strings.mws import *


class TestSolution(unittest.TestCase):
    def test(self):
        self.assertEqual(solution("ADOBECODEBANC", "ABC"), "BANC")
        self.assertEqual(solution("ABABACA", "ABC"), "BAC")
        self.assertEqual(solution("ABCDEF", "XYZ"), "")