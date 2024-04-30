from linked_list import LinkedList
# first in, first out (FIFO)

class Queue:
    def __init__(self) -> None:
        self.data = LinkedList()

    def enqueue(self, value):  # O(1)
        """Add value to back of queue"""
        self.data.add_back(value)

    def dequeue(self):  # O(1)
        """Remove from front of queue"""
        return self.data.delete_front()
