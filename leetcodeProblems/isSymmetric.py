"""
    Problem Statement:
           Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
"""
#node class
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        
class Solution():

    def checkIfSymmetric(self, lst, rst):
        #both reaches last Node
        if lst is None and rst is None:
            return True
        
        if lst is not None and rst is not None and lst.val != rst.val:
            return False
        
        #check left, right val
        #check right, left val equal
        return (lst, rst) and self.checkIfSymmetric(lst.left, rst.right) and self.checkIfSymmetric(lst.right, rst.left)
            
    def isSymmetric(self, tree):
        if tree is None:
            return False
        
        left = tree.left #left sub tree
        right = tree.right #right sub tree
        
        if self.checkIfSymmetric(left, right):
            return True
        else:
            return False
