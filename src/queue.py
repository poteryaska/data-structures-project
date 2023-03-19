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
        if self.head and self.tail is not None:
            old_head = self.head
            if self.head.next_node is not None:
                new_head = self.head.next_node
                del self.head
                self.head = new_head
                return old_head.data
            else:
                self.head = None
                self.tail = None
                return old_head.data

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        all_queues = []
        item = self.tail
        while item is not None:
            all_queues.append(item.data)
        all_queues.reverse()
        return f"{''.join(all_queues)}"
        # return f"{self.head.data}\n{self.head.next_node.data}\n{self.tail.data}"