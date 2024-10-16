# Last in, First Out (LIFO)

class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):  # O(1)
        """Push a value to the top of the stack"""
        self.data.append(value)

    def pop(self):  # O(1)
        """Pop the value off the top of the stack"""
        return self.data.pop()

    def peek(self):  # O(1)
        """Look at the top of the stack (don't remove)"""
        return self.data[-1]

    def __repr__(self) -> str:
        return f'<Stack {self.data}>'

