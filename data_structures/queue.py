# First in, First out (FIFO)

from linked_list import LinkedList

class Queue:
    def __init__(self) -> None:
        self.data = LinkedList()

    def enqueue(self, value):  # O(1)
        '''add to the end of the queue'''
        self.data.add_back(value)

    def dequeue(self):  # O(1)
        '''remove from the front of the queue'''
        return self.data.delete_front()
    
    def is_empty(self):
        return self.data.is_empty()

    def print(self):
        self.data.print_list()


# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.print()
# print('-'*20)
# q.dequeue()
# q.print()
# print('-'*20)
# q.dequeue()
# q.print()