"""
    Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and
    node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's 
    descendants. The tree s could also be considered as a subtree of itself.
"""

class TreeNode(self, val):
    self.val = val
    self.left = None
    self.right = None
 
class Solution():
    
    def isSubTree(self, maintree, subtree):
        #if maintree is none
        if maintree is None:
            return False
        
        if self.isSubTreeUtil(self, maintree, subtree):
            return True
        else:
            left = self.isSubTree(maintree.left, subtree)
            right = self.isSubTree(maintree.right, subtree)
            
            return left or right
    
   #helper function
   def isSubTreeUtil(self, mt, st):
        if mt.val is None or st.val is None:
            return mt.val is None and st.val is None
        
        if(mt.val == st.val):
            l = self.isSubTreeUtil(mt.left, st.left)
            r = self.isSubTreeUtil(mt.right, st.right)
            return l and r
        else:
            return False
