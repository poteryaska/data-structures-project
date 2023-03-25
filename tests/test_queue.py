"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Node, Queue

class TestStack(unittest.TestCase):
    def test_Node(self):
        n1 = Node(1, 2)
        self.assertEqual(n1.data, 1)
        self.assertEqual(n1.next_node, 2)
    def test_Queue(self):
        queue = Queue()
        queue.enqueue('111')
        queue.enqueue('222')
        queue.enqueue('333')
        self.assertEqual(queue.head.data, '111')
        self.assertEqual(queue.head.next_node.data, '222')
        self.assertEqual(queue.tail.data, '333')
        self.assertEqual(str(queue), '111\n222\n333')
        queue.dequeue()
        self.assertEqual(queue.head.data, '222')
        queue.dequeue()
        self.assertEqual(queue.head.data, '333')
        queue.dequeue()
        self.assertEqual(queue.dequeue(), None)


