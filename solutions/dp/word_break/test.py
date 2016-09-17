import unittest
from solutions.dp.word_break import *


class TestSolution(unittest.TestCase):
    def test(self):
        d = {"a", "man", "plan", "panama", "canal"}
        s = "amanaplanacanal"
        p = []
        backtrack(s, d, p)
        self.assertEqual(p, ["a", "man", "a", "plan", "a", "canal"])
        self.assertEqual(dp(s, d), ["a", "man", "a", "plan", "a", "canal"])
