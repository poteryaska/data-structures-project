class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data: dict, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        new_node = Node(data)
        if self.tail is None:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next_node = new_node
            self.tail = self.tail.next_node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string

    def to_list(self):
        '''возвращает список с данными, содержащимися в односвязном списке'''
        node = self.head
        if node is None:
            return None
        ll_list = []
        while node:
            ll_list.append(node.data)
            node = node.next_node
        return ll_list

    def get_data_by_id(self, id):
        '''возвращает первый найденный в LinkedList словарь с ключом 'id',
        значение которого равно переданному в метод значению'''
        for item in self.to_list():
            try:
                if item['id'] == id:
                    return item
            except TypeError:
                print('Данные не являются словарем или в словаре нет id.')
