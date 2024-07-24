class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self) -> str:
        return f'<Node {self.value}>'
    

class LinkedList:
    def __init__(self):
        self.head = None

    def add_back(self, value):  # O(n)
        '''Add a new node to the back of the list'''
        new_node = Node(value)

        if self.head is None:  # this node is the first one
            self.head = new_node
            return
        
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node

    def add_front(self, value):  # O(1)
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete_back(self):  # O(n)
        curr = self.head

        if curr.next is None:  # only one node
            self.head = None
            return

        while curr.next.next is not None:  # second to last node
            curr = curr.next
        curr.next = None

    def delete_front(self):  # O(1)
        self.head = self.head.next

    def print(self):  # O(n)
        curr = self.head
        while curr is not None:
            print(curr)
            curr = curr.next


ll = LinkedList()
ll.add_front(0)
ll.add_front(1)
ll.add_front(2)
ll.print()
print('-'*20)
ll.delete_front()
ll.delete_front()
ll.delete_front()
ll.print()