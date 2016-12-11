import unittest
from problems.sorting.nuts_bolts import *


class TestSolution(unittest.TestCase):
    def test(self):
        n = ['%', '#', '$', '^', '!', '@']
        b = ['$', '^', '!', '#', '@', '%']
        solution(n, b)
        self.assertEqual(n, b)
