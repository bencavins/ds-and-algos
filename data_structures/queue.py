from linked_list import LinkedList

class Queue:
    def __init__(self):
        self.data = LinkedList()

    def enqueue(self, value):
        """Add value to the back of the line"""
        self.data.add_back(value)  # O(1)

    def dequeue(self):
        """Remove from the front of the line"""
        return self.data.delete_front()  # O(1)
