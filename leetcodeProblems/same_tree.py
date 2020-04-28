"""
Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes
have the same value.
"""

class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution():
    
    def util(self, t1, t2):
        if(t1 and not t2):
            return False
        elif(not t1 and t2):
            return False
        elif(not t1 and not t2):
            return True
        elif(t1.val != t2.val):
            return False
        else:
            return self.util(t1.left, t2.left) and self.util(t1.right, t2.right)
            
    def isSameTree(self, t1, t2):
        return self.util(t1, t2)


t1n1, t2n1 = Node(1), Node(1)
t1n2, t2n2 = Node(2), Node(None)
t1n3, t2n3 = Node(3), Node(3)

tree1 = t1n1
tree1.left = t1n2
tree1.right = t1n3

tree2 = t2n1
tree2.left = t2n2
tree2.right = t2n3

print(Solution().isSameTree(tree1, tree2))