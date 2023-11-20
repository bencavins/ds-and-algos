"""
For queues, the first item in is the first item out (FIFO)

Useful for when there are more requests that current resources can handle.
Considered the most fair approach.
"""
from linked_list import LinkedList

class Queue:
    def __init__(self):
        self.data = LinkedList()
    
    def enqueue(self, *args):
        """Add a value to the queue"""
        # O(1)
        for arg in args:
            self.data.add_back(arg)

    def dequeue(self):
        """Remove value from the queue"""
        # O(1)
        return self.data.delete_front()
