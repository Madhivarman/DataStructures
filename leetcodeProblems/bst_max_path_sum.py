class Solution:
    def helperUtil(self, root):
        #left
        if root.left == None:
            left = 0
        else:
            left = self.helperUtil(root.left)
            
        #right
        if root.right == None:
            right = 0
        else:
            right = self.helperUtil(root.right)
        
        self.result = max(self.result, root.val, root.val + left + right)
        return max(0, root.val + max(left, right))
        
        
    def maxPathSum(self, root):        
        self.result=-math.inf
        self.helperUtil(root)
        return self.result
