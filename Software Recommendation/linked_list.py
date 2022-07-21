from node import Node

class SLL:
    def __init__(self, value=None):
        self.head_node = Node(value)
    
    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, value):
        new_node = Node(value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def remove_node(self, value):
        curr = self.head_node
        if curr.get_value() == value:
            self.head_node = curr.get_next_node()
        else:
            while curr:
                n_node = curr.get_next_node()
                if n_node.get_value() == value:
                    curr.next_node = n_node.get_next_node()
                    curr = None
                else:
                    curr = n_node

    def stringify_list(self):
        lst = ""
        curr = self.head_node
        while curr:
            lst += str(curr) + '\n'
            curr = curr.next_node
        return lst