
class Node():
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


class List():
    def __init__(self):
        self.head   = None
        self.n_elem = 0

    def push(self, data):
        self.head = Node(data)
        self.n_elem += 1

    def pop(self):
        if self.head == None:
            return None
        temp = self.head
        self.head = self.head.next
        self.n_elem -= 1
        return temp.data

