import queue


class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


    def __repr__(self):
        return f"{self.data}"


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def enqueue(self, data: str):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        if self.tail is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next_node = Node(data)
            self.tail = self.tail.next_node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head is not None:
            data = self.head.data
            self.head = self.head.next_node
            return data
        else:
            return None

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        if not self.head:
            return ''
        all_queues = []
        head = self.head
        while head:
            all_queues.append(head.data)
            head = head.next_node
        return '\n'.join(all_queues)
