import unittest
from problems.strings.regex import *


class TestSolution(unittest.TestCase):
    def test(self):
        self.assertTrue(match("a*c", "abc"))
        self.assertTrue(match("a*c", "abbbc"))
        self.assertFalse(match("a.c", "abbc"))
