"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Node, Stack

class TestStack(unittest.TestCase):
    def test_Node(self):
        n1 = Node(1, 2)
        self.assertEqual(n1.data, 1)
        self.assertEqual(n1.next_node, 2)
    def test_Stack(self):
        stack = Stack()
        stack.push('555')
        stack.push('666')
        self.assertEqual(stack.top.next_node.data, '555')
        stack.pop()
        self.assertEqual(stack.top.data, '555')


