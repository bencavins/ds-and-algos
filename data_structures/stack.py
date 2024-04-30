# Last in, First out (LIFO)

class Stack:
    def __init__(self) -> None:
        self.data = []

    def push(self, value): # O(1)
        """Adds a new value to the top of the stack"""
        self.data.append(value)

    def pop(self): # O(1)
        """Removes the value from the top of the stack"""
        return self.data.pop()
    
    def peek(self):
        return self.data[-1]

s = Stack()