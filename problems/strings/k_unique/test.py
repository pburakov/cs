import unittest
from problems.strings.k_unique import *


class TestSolution(unittest.TestCase):
    def test(self):
        self.assertEqual(recursive("zzzababcdabef", 2), 4)
        self.assertEqual(recursive("abcdef", 2), 2)
        self.assertEqual(recursive("", 2), 0)
