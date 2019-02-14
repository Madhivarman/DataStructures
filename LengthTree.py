class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def size(root):
    if root is None:
        return 0
    else:
        return (size(root.left) + 1 + size(root.right))

root = Node(30)
root.left = Node(20)
root.right = Node(50)
root.left.left = Node(100)
root.left.right = Node(150)
root.right.left = Node(200)

print("Size of the tree is: {}".format(size(root)))
