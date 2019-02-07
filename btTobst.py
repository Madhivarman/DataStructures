class Node:
    """Initial Class Declaration"""
    def __init__(self, key):
        self.val = key
        self.right = None
        self.left = None

"""do Inorder Traversal"""
def doInorderTraversal(root, temp):
    if root is None:
        return

    #first store the left structure
    doInorderTraversal(root.left, temp)
    temp.append(root.val)
    doInorderTraversal(root.right, temp)
    #return the temp
    return temp

"""convert BinaryTree to Binary Search Tree"""
def convertBTToBST(arr, root):
    #if root is null just return empty array
    if root is None:
        return

    """do Inorder Traversal here"""
    convertBTToBST(arr, root.left)
    root.val = arr[0] #set the array val
    arr.pop(0) #pop the first element
    convertBTToBST(arr, root.right)


def storeInArray(root):
    """do inorder traversal"""
    arr = doInorderTraversal(root, temp)
    return arr

def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.val)
        inorderTraversal(root.right)

root = Node(50)
root.left = Node(100)
root.right = Node(30)
root.left.left = Node(70)
root.right.right = Node(150)
root.right.left = Node(200)

temp = [] #to store temporary array
array = storeInArray(root)
sortedArray = sorted(array, reverse=False) #sort an array
convertBTToBST(sortedArray, root)
print("After converting BT to BST")
print(inorderTraversal(root))
