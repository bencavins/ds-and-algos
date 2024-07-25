class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self) -> str:
        return f"<Node {self.value}>"

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # O(1)
    def add_front(self, value):
        if self.head is None:  # our list is empty
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
    
    # O(1)
    def add_back(self, value):
        new_node = Node(value)
        if self.head is None:  # list is empty
            self.add_front(value)
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    # O(1)
    def delete_front(self):
        val = self.head.value
        if self.head is not None:
            self.head = self.head.next
        elif self.head.next is None:
            self.head = None
            self.tail = None
        return val
    
    # O(n)
    def delete_back(self):
        curr_node = self.head
        if self.head.next is None:
            self.head = None
        else:
            while curr_node.next is not self.tail:
                curr_node = curr_node.next
            self.tail = curr_node
            self.tail.next = None
    
    # O(n)
    def index(self, i):
        pass

    def is_empty(self):
        return self.head is None

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node)
            # move to next node in list
            current_node = current_node.next

ll = LinkedList()