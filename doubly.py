class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def pushOn(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        if self.head is self.tail:
            self.tail = new_node
            self.tail.prev = self.head
            self.head.next = self.tail
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    def traverse(self):
        curr = self.head
        while curr:
            print(curr.val, end=" --> ")
            curr = curr.next
        print(None)

    def inverseTraverse(self):
        curr = self.tail
        while curr:
            print(curr.val, end=" --> ")
            curr = curr.prev
        print(None)

    def insertAfter(self, new_value, existing_value):
        new_node = Node(new_value)
        i = self.head
        j = self.tail
        while True:
            if i.val == existing_value:
                curr = i
                break
            if j.val == existing_value:
                curr = j
                break
            if i is j:
                break
            i = i.next
            j = j.prev
        
        temp = curr.next
        curr.next = new_node
        new_node.prev = curr
        temp.prev = new_node
        new_node.next = temp

        


d = DoublyLinkedList()
d.pushOn(3)
d.pushOn(4)
d.pushOn(7)
d.insertAfter(5, 4)
d.traverse()