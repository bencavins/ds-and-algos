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

    def depth_first_search(self, target):
        def helper(node):
            if node is None:  # base case
                return
            
            # in-order traversal 
            # check the left branch
            helper(node.left)
            # check the current node
            print(node)
            # check the right branch
            helper(node.right)

            # pre-order traversal
            # print(node)
            # helper(node.left)
            # helper(node.right)

            # post-order traversal
            # helper(node.left)
            # helper(node.right)
            # print(node)

        helper(self.root) # kick off the recursive loop

    def breadth_first_search(self, target):
        q = Queue()
        q.enqueue(self.root)

        while not q.is_empty():
            node = q.dequeue()
            print(node)

            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)

    def binary_search(self, target):
        curr = self.root
        while curr is not None:
            # check the current node
            if curr.value == target:
                return True
            
            if target < curr.value:
                curr = curr.left
            else: # >
                curr = curr.right

        # target value doesn't exist
        return False
    


t = BinarySearchTree()

t.root = Node(5)
t.root.left = Node(2)
t.root.left.left = Node(1)
t.root.left.right = Node(3)
t.root.right = Node(7)
t.root.right.left = Node(6)
t.root.right.right = Node(8)


t.breadth_first_search(10)