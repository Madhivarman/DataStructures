"""
  Problem Statement:
    Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).
"""

class TreeNode():
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    
class Solution:
    
    def dfs(self, tree, level, stack):
        if level >= len(stack):
            stack.append([])
        
        if tree:
            stack[level-1].append(tree.val)
        else:
            return
        
        self.dfs(tree.left, level+1, stack)
        self.dfs(tree.right, level+1, stack)
        
        return stack
    
    def largestValues(self, root: TreeNode) -> List[int]:
        result = []
        
        if root is None:
            return result
        
        temp = self.dfs(root, 1, [])
        
        for l in temp:
            if len(l) != 0:
                result.append(max(l))
        
        return result
        
        
        
