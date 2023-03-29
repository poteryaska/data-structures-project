"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""

import unittest
from src.linked_list import Node, LinkedList

class TestStack(unittest.TestCase):
    def test_Node(self):
        n1 = Node({'id': 1})
        self.assertEqual(n1.data, {'id': 1})

    def test_LinkedList(self):
        list = LinkedList()
        list.insert_at_end({'id': 1})
        self.assertEqual(list.head.data, {'id': 1})
        self.assertEqual(list.tail.data, {'id': 1})
        list.insert_at_end({'id': 2})
        list.insert_beginning({'id': 0})
        list.insert_at_end({'id': 3})
        self.assertEqual(list.tail.data, {'id': 3})
        self.assertEqual(list.head.data, {'id': 0})
        self.assertEqual(list.tail.next_node, None)
        self.assertEqual(str(list), " {'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")