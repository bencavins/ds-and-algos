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
    
    def dfs(self):
        '''Depth-first Search'''
        def helper(node):
            if node is None:
                return
            
            # pre-order traversal
            # print(node)  # process the current node
            # helper(node.left)  # process the left branch
            # helper(node.right)  # process the right branch

            # # in-order traversal
            helper(node.right)  # process the right branch
            print(node)  # process the current node
            helper(node.left)  # process the left branch

            # post-order traversal
            # helper(node.left)  # process the left branch
            # helper(node.right)  # process the right branch
            # print(node)  # process the current node
        
        helper(self.root)


    def bfs(self):
        '''Breadth-first Search'''
        q = Queue()
        q.enqueue(self.root)
        while not q.is_empty():
            curr = q.dequeue()  # grab the next node in the queue
            print(curr)  # process current node
            if curr.left:
                q.enqueue(curr.left)  # add left node to the queue
            if curr.right:
                q.enqueue(curr.right) # add right node to the queue
        
            

    def binary_search(self, value):
        curr = self.root
        while curr is not None:
            # check if this node is the one we are looking for
            if curr.value == value:
                return True
            
            # decide which branch to go down
            if value < curr.value:
                curr = curr.left
            else:
                curr = curr.right
        return False




t = BinarySearchTree()
t.root = Node(5)
t.root.left = Node(3)
t.root.left.left = Node(1)
t.root.left.right = Node(4)
t.root.right = Node(7)
t.root.right.right = Node(8)