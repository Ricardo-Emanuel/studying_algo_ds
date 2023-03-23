class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self._head = Node(None)
        self._len = 0

    def create(self, data):
        node = Node(data)
        self._head = node
        self._len += 1

    def append(self, data):
        if self._len == 0:
            self.create(data)
            return
        node = Node(data)
        temp = self._head
        while (temp.next != None):
            temp = temp.next
        temp.next = node
        self._len += 1

    def prepend(self, data):
        node = Node(data)
        node.next = self._head
        self._head = node
        self._len += 1
    
    def deleteHead(self):
        if self._len == 0:
            print("The linked list is empty")
            return
        self._head = self._head.next if self._len else None
        self._len -= 1

    def deleteTail(self):
        if self._len == 0:
            print("The linked list is empty")
            return
        elif self._len == 1:
            self._head = None
            self.tail = None
            self._len -= 1
        temp = self._head
        for i in range(self._len - 1):
            temp = temp.next
        self.tail = temp
        self._len -= 1

    def deleteAt(self, index):
        if self._len == 0:
            print("The linked list is empty")
            return
        if index == 0:
            self.deleteHead()
            return
        if index == -1 or index == self._len - 1:
            self.deleteTail()
            return
        temp = self._head
        for i in range(index - 1):
            temp = temp.next
        temp.next = temp.next.next
        self._len -= 1

    def __len__(self):
        return self._len
    
    def print(self):
        temp = self._head
        while temp != None:
            print(temp.data, " ", end="")
            temp = temp.next

if __name__ == "__main__":
    ll = LinkedList()