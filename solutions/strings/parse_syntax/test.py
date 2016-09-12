import unittest
from solutions.strings.parse_syntax import *


class TestSolution(unittest.TestCase):
    def test(self):
        self.assertEquals(solution("ab4c"), "abcccc")
        self.assertEquals(solution("ab0c"), "ab")
        self.assertEquals(solution("2[a2bc]"), "abbcabbc")
        self.assertEquals(solution("2[ab3[cd]]x3yz"), "abcdcdcdabcdcdcdxyyyz")
        self.assertEquals(solution("[]"), "")
        self.assertEquals(solution("a"), "a")
