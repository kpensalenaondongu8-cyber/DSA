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