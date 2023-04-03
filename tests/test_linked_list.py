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

    def test_LinkedList_1(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        self.assertEqual(ll.to_list(), [{'id': 1, 'username': 'lazzy508509'},
                                        {'id': 2, 'username': 'mik.roz'},
                                        {'id': 3, 'username': 'mosh_s'}])
        self.assertEqual(ll.get_data_by_id(3), {'id': 3, 'username': 'mosh_s'})
        ll.insert_at_end({'222'})
        # self.assertRa(ll.get_data_by_id(4), TypeError'Данные не являются словарем или в словаре нет id.')