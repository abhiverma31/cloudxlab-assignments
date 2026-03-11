class Node:
    left = None
    right = None
    def __init__(self, value):
        self.value = value
    def print_sorted(self, node):
        if node is None:
            return
        self.print_sorted(node.left)
        print(node.value)
        self.print_sorted(node.right)
    def search(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self.search(node.left, value)
        elif value > node.value:
            return self.search(node.right, value)
    def insert(self, node):
        if node is None:
            return self
        elif node.value <= self.value:
            if self.left is not None:
                self.left = self.left.insert(node)  
            elif self.left is None:    
                self.left = node    
        else:
            if self.right is not None:
                self.right = self.right.insert(node)
            elif self.right is None:
               self.right = node    
            
        return self 
    
def test_bst_functionalities():
    # insert elements to tree
    root = Node(5)
    root = root.insert(None)

    node1 = Node(3)
    root = root.insert(node1)

    node2 = Node(2)
    root = root.insert(node2)

    node3 = Node(4)
    root = root.insert(node3)

    node4 = Node(1)
    root = root.insert(node4)

    #########################################

    # print tree in sorted order
    root.print_sorted(root)

    #########################################
    print()

    # search an element in tree
    print(root.search(root, 1))
    print(root.search(root, 4))
    print(root.search(root, 19))  
    
test_bst_functionalities()     