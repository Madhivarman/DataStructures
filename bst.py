class Node:
    
    """Initialization of Node"""
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
    
"""Inserting the node"""
def insert(root, node):

        if root is None:
            root = node
        else:
            #check if the key is lesser than root then append left
            if root.val > node.val:
                if root.left is None:
                    root.left = node
                else:
                    insert(root.left, node)
            else:
                if root.val < node.val:
                    if root.right is None:
                        root.right = node
                    else:
                        insert(root.right, node)

def getMinimumValue(rootNode):
    current = rootNode
    while(current.left is not None):
        current = current.left

    return current

"""deleting the node"""
def deleteNode(root, key):
    
    print("*" * 20)
    print("DELETING THE NODE")
    print("*" * 20)

    """if root is None then return None"""
    if root.val is None:
        return root

    if root.val < key:
        root.right = deleteNode(root.right, key)
    elif root.val > key:
        root.left = deleteNode(root.left, key)
    else:
        if root.val is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        #if key is found
        temp = getMinimumValue(root.right)
        root.val = temp.val
        #delete the node
        root.right = deleteNode(root.right, temp.val)


    return root



"""Print the Traversal"""
def traversal(root):
        if root:
            traversal(root.left)
            print(root.val)
            traversal(root.right)


#create an Object 
node = Node(50)

#insert an data as
insert(node, Node(25))
insert(node, Node(60))
insert(node, Node(10))
insert(node, Node(70))
insert(node, Node(100))
insert(node, Node(12))
insert(node, Node(80))

#Inorder Traversal
print(traversal(node))

deleteNode(node, 70)
print(traversal(node))
