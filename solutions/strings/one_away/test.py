import unittest
from solutions.strings.one_away import *


class TestSolution(unittest.TestCase):
    def test(self):
        self.assertTrue(solution("pale", "ale"))
        self.assertTrue(solution("ple", "pale"))
        self.assertTrue(solution("pale", "gale"))
        self.assertFalse(solution("pale", "bake"))
        self.assertFalse(solution("pale", "bob"))
