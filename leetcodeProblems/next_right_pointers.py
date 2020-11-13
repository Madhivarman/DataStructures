"""
 Problem Statement:
    You are given a perfect binary tree where all leaves are on the same level, and every parent has two children
    Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
    Initially, all next pointers are set to NULL.
"""

class TreeNode():
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    self.next = None


class Solution():
  def connect(self, root:TreeNode) -> TreeNode:
     if not root:
        return root
     
     above, below = root, root.left
     
     while below:
        curr = below
        #level order traversal
        while above:
          if curr = above.left:
              curr.next = above.right
              above = above.next
           else:
              curr.next = above.left
           curr = curr.next
           
        #updating the pointers
        above = below
        below = above.left
    
    return root
