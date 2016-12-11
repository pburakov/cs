import unittest
from problems.graphs.snakes_ladders import *


class TestSolution(unittest.TestCase):
    def test(self):
        board = [0, 0, 0, 7, 2, 0, 0, 0, 5, 0]
        self.assertEqual(solution(board), 2)
