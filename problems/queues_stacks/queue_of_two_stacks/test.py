import unittest
from problems.queues_stacks.queue_of_two_stacks import *


class TestSolution(unittest.TestCase):
    def test(self):
        q = Queue()
        for i in range(1, 10):
            q.enqueue(i)
        for i in range(1, 10):
            self.assertEqual(q.dequeue(), i)
        with self.assertRaises(IndexError) as cm:
            q.dequeue()
