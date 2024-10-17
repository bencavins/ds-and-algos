class Node:
    def __init__(self, value):
        self.value = value
        # self.left = None
        # self.right = None
        self.branches = []
        # self.count = 0

    def __repr__(self) -> str:
        return f'<Node {self.value}>'


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, new_value):
        current_node = self.root
        while True:
            if new_value < current_node.value:
                # check left branch
                if current_node.left is None:
                    current_node.left = Node(new_value)
                    return
                else:
                    current_node = current_node.left
            else:  # value >= current_node.value
                # check right branch
                if current_node.right is None:
                    current_node.right = Node(new_value)
                    return
                else:
                    current_node = current_node.right
        
    def search(self, target):
        curr = self.root
        while curr is not None:
            print('loop cycle')
            # check the current node
            if curr.value == target:
                return True
            
            if target < curr.value:
                curr = curr.left
            else: # >=
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

print(t.search(3))
# print(t.search(99))
