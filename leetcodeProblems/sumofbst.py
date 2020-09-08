class Solution:
    
    def dfs(self, root, s):
        if root:
            s += str(root.val)
            if not root.left and not root.right:
                self.ans += int(s, 2)
                return 
            
            self.dfs(root.left, s)
            self.dfs(root.right, s)
        
        return 
    
    def sumRootToLeaf(self, root: TreeNode) -> int:
        s = ''
        self.ans = 0
        self.dfs(root, s)
        return self.ans
