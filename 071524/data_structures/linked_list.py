class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self) -> str:
        return f'<Node {self.value}>'


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next
        
    def append(self, value):  # O(1)
        new_node = Node(value)
        if self.is_empty():
            self.add_front(value)
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def prepend(self, value): # O(1)
        if self.is_empty():
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node

    def delete_front(self):  # O(1)
        val = self.head.value
        if self.head is not None:
            self.head = self.head.next
        elif self.head.next is None:
            self.head = None
            self.tail = None
        return val
    
    def delete_back(self):  # O(n)
        curr_node = self.head
        if self.head.next is None:
            self.head = None
        else:
            while curr_node.next is not self.tail:
                curr_node = curr_node.next
            self.tail = curr_node
            self.tail.next = None
    
    def is_empty(self):
        return self.head is None


ll = LinkedList()
