class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data: int):
        self.head = Node(data)
        self.len = 1

    def create(self, data):
        node = Node(data)
        self.head = node
        self.len += 1

    def append(self, data):
        node = Node(data)
        temp = self.head
        while (temp.next != None):
            temp = temp.next
        temp.next = node
        self.len += 1

    def prepend(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.len += 1

    def deleteAt(self, index):
        ...

    def __len__(self):
        return self.len

if __name__ == "__main__":
    ll = LinkedList(1)