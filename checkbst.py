class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def isBST(root, l=None, r=None):
    if root is None:
        return True
    
    if (l != None and root.key < l.key):
        return False

    if (l != None and root.key > r.key):
        return False

    return isBST(root.left, l, root) and isBST(root.right, root, r)

node = Node(4)
node.left = Node(2)
node.right = Node(5)
node.left.left = Node(1)
node.left.right = Node(0)

if isBST(node):
    print("Yes, It's BST")
else:
    print("No")
