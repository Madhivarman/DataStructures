"""
    Problem Statement:
        Given a binary tree, return the sum of values of nodes with even-valued grandparent.  
        (A grandparent of a node is the parent of its parent, if it exists.)
        If there are no nodes with an even-valued grandparent, return 0.
"""
class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution():
    def helperUtil(self, stack, tree):
        level = 0
        #stack structure - (val, level, parent, grandparent)
        stack.append((tree, tree.val, level, 0, 0))
        #iterate till the stack is empty
        while stack:
            size = len(stack)
            i = 0
            while(i < size):
                subtree, nodeval, level, p, gp = stack.pop()
                #print(nodeval, level, p, gp)
                #condition check
                if level >= 2:
                    if gp % 2 == 0 and gp != 0:
                        self.totalSum += nodeval
                if subtree.left is not None:
                    gp = p
                    stack.append((subtree.left, subtree.left.val, level+1, nodeval, gp))
                if subtree.right is not None:
                    gp = p
                    stack.append((subtree.right, subtree.right.val, level+1, nodeval, gp))
                
                i += 1 #increment the pointer

    def sumEvenGrandParentElem(self, tree):
        totalSum = 0
        stack = []
        self.helperUtil(stack, tree)
        return totalSum
