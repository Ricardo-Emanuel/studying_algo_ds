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
    
    def deleteHead(self):
        self.head = self.head.next
        self.len -= 1

    def deleteTail(self):
        temp = self.head
        for i in range(self.len - 1):
            self.tail = temp
        self.len -= 1

    def deleteAt(self, index):
        if index == 0:
            self.deleteHead()
            return
        if index == -1 or index == self.len - 1:
            self.deleteTail()
            return
        temp = self.head
        for i in range(index - 1):
            temp = temp.next
        temp.next = temp.next.next
        self.len -= 1

    def __len__(self):
        return self.len
    
    def print(self):
        temp = self.head
        while temp != None:
            print(temp.data, " ", end="")
            temp = temp.next

if __name__ == "__main__":
    ll = LinkedList(1)