class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
         new_node = Node(value)     
         if self.head is None:
             self.head = new_node
         else:
             current = self.head
             while current.next is not None:
                current += 1
                current = new_node               
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

first = Node(10)
second = Node(20)
third = Node(30)
first.next = second
second.next = third

current = first
while current is not None:
    print(current.value)
    current = current.next
