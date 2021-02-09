"""
  Problem Statement:
      Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree 
      so that all its elements lies in [low, high]. Trimming the tree should not change the relative structure of the 
      elements that will remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven 
      that there is a unique answer.

      Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.
"""

class TreeNode:
  def __init__(self, val):
      self.val = val
      self.left = None
      self.right = None
      

class Solution:
    def trimBST(self, node: TreeNode, low: int, high: int) -> TreeNode:
            if node is None:
                return
            
            if node.val < low:
                return self.trimBST(node.right, low, high)
            
            elif node.val > high:
                return self.trimBST(node.left, low, high)
            
            else:
                node.left = self.trimBST(node.left, low, high)
                node.right = self.trimBST(node.right, low, high)
                return node
