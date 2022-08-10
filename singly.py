# create a linked list object that has the following methods
# append - add a new node to the end of the LL
# insertAfter -- insert a new node after another node of a given value 
#     list.insertAfter(new_value, existingNodeValue)
# traverse -- print all values
# reverse -- reverse the list in-place

# create base class
class LinkedList:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    def append(self, value): # O(n)
        curr = self
        while curr.next:
            curr = curr.next
        curr.next = LinkedList(value)
    def traverse(self):
        curr = self
        while curr:
            print(curr.val, end= " -> ")
            curr = curr.next
        print('None')
    def insertAfter(self, new_value, existing_value):
        curr = self
        while curr and curr.val != existing_value:
            curr = curr.next
        if not curr:
            return "existing value param does not exist in this list!"
        temp = curr.next
        new_node = LinkedList(new_value)
        curr.next = new_node
        new_node.next = temp
    def reverse(self):
        prev = None
        curr = self
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        prev.traverse()
        return prev

def reverseRecursion(node, prev=None):
    if not node:
        return prev
    temp = node.next
    node.next = prev
    return reverseRecursion(temp, prev=node)




head = LinkedList(1)
head.append(2)
head.append(3)
head.append(4)
head.traverse()
reverseRecursion(head).traverse()




 