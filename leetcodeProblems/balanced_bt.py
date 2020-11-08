"""
  Problem Statement:
      Given a binary tree, determine if it is height-balanced.
      For this problem, a height-balanced binary tree is defined as:
        a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
"""
class TreeNode():
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    
class Solution:
    #this function returns height
    def dfs(self, node):
        if not node:
            return 0
        return 1 + max(self.dfs(node.left), self.dfs(node.right))
    
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return abs(self.dfs(root.left) - self.dfs(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
