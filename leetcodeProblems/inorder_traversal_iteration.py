"""
Given a binary tree, return the inorder traversal of its nodes' values.
"""
class Node():
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution():
    def inOrderTraversal(self, root):
        current = root
        stack = []
        done = 0
        result = []

        while(True):
            #append to the stack till you reach the left element null
            if current is not None:
                stack.append(current)
                current = current.left
            
            #backtrack
            elif(stack):
                current = stack.pop()
                result.append(current.data) #append the value
                current = current.right #set the current value right
            else:
                break

        return result


#define tree
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

root = n1
root.left = n2
root.right = n3
root.left.left = n4
root.left.right = n5

print(Solution().inOrderTraversal(root))