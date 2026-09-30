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
