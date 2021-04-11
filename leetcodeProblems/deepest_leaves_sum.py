class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution: 
    def dfs(self, node, level):
        
        if node is None:
            return
        
        if len(self.stack) <= level:
            self.stack.append([]) #append one extra depth
        
        if node:
            self.stack[level].append(node.val)
        
        self.dfs(node.left, level+1)
        self.dfs(node.right, level+1)
        
        
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.stack = []
        level = 0
        self.dfs(root, level)
        return sum(self.stack[-1])
        
