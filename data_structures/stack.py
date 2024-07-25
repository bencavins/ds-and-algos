# Last in, First out (LIFO)

class Stack:
    def __init__(self) -> None:
        self.data = []

    def push(self, value):  # O(1)
        '''adds to the top of the stack'''
        self.data.append(value)

    def pop(self):  # O(1)
        '''removes the item at the top of the stack'''
        return self.data.pop()

    def peek(self):  # O(1)
        '''look at the top of the stack'''
        return self.data[-1]
    
    def __repr__(self) -> str:
        return f'<Stack {self.data} <~ top>'
    

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s)
s.pop()
print(s)
s.pop()
print(s)
