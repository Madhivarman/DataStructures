""" Considering each Number as a Node"""
class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def inorder(root):

	temp = []
	if root:
		inorder(root.left)
		temp.append(root.val)
		inorder(root.right)

	return temp

def checkNodeIsBT(root):
    """default will be False"""
    boolean = False
    if root is None:
        boolean = True
        return boolean

    #create an queue to keep track
    q, queue = [], []
    q.append(root) #append the tree

    arr = inorder(root)
    checkpoint = len(arr)
    num  = 0 #create an pointer

    while(num < checkpoint):
    	node = q[0] #create an pointer
    	q.pop(0) #pop an node from the queue

    	#write an condition
    	if node.left == None and node.right = None:
    		boolean = True
    		continue

    	if node.left == None or node.right == None:
    		boolean = False
    		return boolean

    	queue.append(node.left)
    	queue.append(node.right)

    	num += 1 #increment the counter


def checkResult(result):
    if result:
        print("Yes!!!")
    else:
        print("No :(")

#set 1
root = Node(50)
root.left = Node(20)
root.right = Node(70)
root.right.left = Node(90)
root.right.right = Node(100)

result = checkNodeIsBT(root)
checkResult(result)

#set 2
root1 = Node(150)
root1.left = Node(70)
root1.right = Node(100)
root1.right.right = Node(90)

result = checkNodeIsBT(root)
checkResult(result)
