"""
For stacks, the last item in is the first item taken out (LIFO)

Useful for tracking history (for example, an undo command)
"""

class Stack:
    def __init__(self):
        self.data = []
    
    def push(self, value):
        # O(1)
        self.data.append(value)

    def pop(self):
        # O(1)
        return self.data.pop()
