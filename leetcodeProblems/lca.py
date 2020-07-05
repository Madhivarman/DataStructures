"""
  Problem Statement:
    Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
    According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest 
    node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

    Given the following binary tree:  
    root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    output = 3
  
"""
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def helperUtil(self, tree, p, q):
        if tree is None:
            return
        if tree == p or tree == q:
            return tree
        
        l = self.helperUtil(tree.left, p, q) 
        r = self.helperUtil(tree.right, p, q)
        
        #if r is None:
            #return None
        
        if l is not None and r is not None:
            return tree
        
        return l or r
        
    
    def lowestCommonAncestor(self, root, p, q):
        if root == p or root == q:
            return root
        
        lst = self.helperUtil(root.left, p, q)
        rst = self.helperUtil(root.right, p, q)
        
        #print(lst, rst)
        
        if lst is None and rst is not None:
            return rst
        
        if lst is not None and rst is None:
            return lst
        
        if lst is not None and rst is not None:
            return root
        
        return root
