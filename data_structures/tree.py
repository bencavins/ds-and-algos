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
        if not self.root:
            return
        
        q = Queue()
        q.enqueue(self.root)

        while not q.is_empty():
            curr_node = q.dequeue()
            print(curr_node)
            if curr_node.left:
                q.enqueue(curr_node.left)
            if curr_node.right:
                q.enqueue(curr_node.right)
        
    def dfs(self):
        def traverse(node):
            if node is None:  # base case
                return
            
            # print(node)  # pre order traversal
            traverse(node.left)
            print(node)  # in order traversal
            traverse(node.right)
            # print(node)  # post order traversal
        traverse(self.root)
    
    def add(self, new_value):
        if self.root is None:
            self.root = Node(new_value)
            return
        
        curr_node = self.root
        while True:
            if new_value < curr_node.value:
                if curr_node.left is None:
                    curr_node.left = Node(new_value)
                    return
                else:
                    curr_node = curr_node.left
            else:  # new_value >= curr_node.value
                if curr_node.right is None:
                    curr_node.right = Node(new_value)
                    return
                else:
                    curr_node = curr_node.right




t = BinarySearchTree()
t.root = Node(5)
t.root.left = Node(3)
t.root.left.right = Node(4)
t.root.left.left = Node(2)
t.root.left.left.left = Node(1)
t.root.right = Node(7)
t.root.right.left = Node(6)
t.root.right.right = Node(10)