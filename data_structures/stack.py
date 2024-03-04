# LIFO (Last in, First Out)

class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        """Add value to the top of the stack"""
        self.data.append(value)  # O(1)

    def pop(self):
        """Remove value from the top of the stack"""
        return self.data.pop()  # O(1)