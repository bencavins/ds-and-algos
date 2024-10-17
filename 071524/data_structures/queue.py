# First in, First out (FIFO)

from linked_list import LinkedList

class Queue:
    def __init__(self) -> None:
        self.data = LinkedList()

    def enqueue(self, value):  # O(1)
        """Adding to the end of the queue"""
        self.data.add_back(value)

    def dequeue(self):  # O(1)
        """Removing from the front of the queue"""
        return self.data.delete_front()

    def peek(self):  # O(1)
        """See who is next in the queue"""
        return self.data.head
    
    def print_queue(self):
        self.data.print_list()
