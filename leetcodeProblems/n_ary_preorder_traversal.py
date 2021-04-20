"""
    Problem Statement:
      Given the root of an n-ary tree, return the preorder traversal of its nodes' values.
      Nary-Tree input serialization is represented in their level order traversal. Each group of children 
      is separated by the null value (See examples)
"""

class Node:
  def __init__(self, val=None, children=None):
    self.val = val
    self.children=None
    
    
    
class Solution:
    def dfs(self,root):
        if root is None:
            return
        
        self.result.append(root.val)
        
        for childobj in root.children:
            self.dfs(childobj)
        
    def preorder(self, root: 'Node') -> List[int]:
        self.result = []
        self.dfs(root)
        return self.result
