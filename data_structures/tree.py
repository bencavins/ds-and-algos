from queue import Queue

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __repr__(self) -> str:
        return f"<Node {self.value}>"


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def bfs(self):
        if self.root is None:
            return
        q = Queue()
        q.enqueue(self.root)
        while not q.is_empty():
            curr = q.dequeue()
            print(curr)
            if curr.left:
                q.enqueue(curr.left)
            if curr.right:
                q.enqueue(curr.right)
    
    def dfs(self):
        def traverse(node):
            if node is None:
                return
            if node.left:
                traverse(node.left)
            print(node)
            if node.right:
                traverse(node.right)
        traverse(self.root)
    
    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        
        curr = self.root
        while True:
            if value < curr.value:
                if curr.left is None:
                    curr.left = Node(value)
                    return
                else:
                    curr = curr.left
            else:
                if curr.right is None:
                    curr.right = Node(value)
                    return
                else:
                    curr = curr.right


t = BinarySearchTree()
t.root = Node(5)
t.root.left = Node(3)
t.root.left.right = Node(4)
t.root.left.left = Node(2)
t.root.left.left.left = Node(1)
t.root.right = Node(7)
t.root.right.left = Node(6)
t.root.right.right = Node(10)
