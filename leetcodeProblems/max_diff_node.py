"""
    Problem Statement:
        Given the root of a binary tree, find the maximum value V for which there exist different nodes A and B 
        where V = |A.val - B.val| and A is an ancestor of B.

        A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.
"""
class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def dfs(self, root, low, high):
        if not root:
            return
        
        self.result = max(self.result, abs(root.val - low), abs(root.val - high))
        
        low = min(root.val, low)
        high = max(root.val, high)
        
        #traverse
        self.dfs(root.left, low, high)
        self.dfs(root.right, low, high)
            
        return self.result
    
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.result = 0        
        self.dfs(root, root.val, root.val)
        return self.result