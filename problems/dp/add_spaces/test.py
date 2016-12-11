import unittest
from problems.dp.add_spaces import *


class TestSolution(unittest.TestCase):
    def test(self):
        d1 = {"this", "is", "favorite", "food"}
        s1 = "thisismikesfavoritefood"
        d2 = {"brother", "looked", "just", "like", "her"}
        s2 = "jesslookedjustliketimherbrother"
        self.assertEqual(solution(s1, d1), "this is mikes favorite food")
        self.assertEqual(solution(s2, d2), "jess looked just like tim her brother")
