import unittest
from solutions.graphs.word_ladder import *


class TestSolution(unittest.TestCase):
    def test(self):
        d = {"hot", "hit", "dot", "dog", "cog", "lot", "log"}
        self.assertEqual(solution(d, "hit", "cog"), ['hit', 'hot', 'dot', 'dog', 'cog'])
