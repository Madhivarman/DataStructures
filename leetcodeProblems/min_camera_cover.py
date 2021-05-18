#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.camera = 0
        #dfs
        ans = self.dfs(root)
        #base condition
        if ans == 0:
            return self.camera + 1
        return self.camera
    
    def dfs(self, root: TreeNode):
        # 0 -> No camera is covered
        # 1 -> covered by camera
        # 2 -> has camera
        if root is None:
            return 1
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        #condition
        #cover  the children with camera
        if left == 0 or right == 0:
            self.camera += 1
            return 2
        #if any of the children has camera, the parent
        #node doesn't have to be covered
        elif left == 2 or right == 2:
            return 1
        else:
            return 0
        
        return self.camera
