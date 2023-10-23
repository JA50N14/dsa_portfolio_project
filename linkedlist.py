from node import Node
class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def insert_beginning(self, value):
        new_node = Node(value)
        new_node.set_link_node(self.head_node)
        self.head_node = new_node

    def get_head_node(self):
        return self.head_node







