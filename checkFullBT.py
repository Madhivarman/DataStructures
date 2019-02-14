class Node:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None

def checkFullBT(root):
    if root is None:
        return True

    if root.left is None and root.right is None:
        return True

    if root.left is not None and root.right is not None:
        return (checkFullBT(root.left) and checkFullBT(root.right))

    return False

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(0)
root.left.right = Node(100)

if checkFullBT(root):
    print("Yes, Its obeys the rule")
else:
    print("No")
