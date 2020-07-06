# Definition for a binary tree node.
class Solution:
    def inorderTraversal(self, root):
        if root is None:
            return
        
        self.inorderTraversal(root.left)
        
        #main logic
        if(self.firstEle is None and self.prevEle.val >= root.val):
            self.firstEle = self.prevEle
        
        if(self.firstEle is not None and self.prevEle.val >= root.val):
            self.secondEle = root
        
        self.prevEle = root
        self.inorderTraversal(root.right)
        
    def recoverTree(self, root):
        self.firstEle = None
        self.secondEle = None
        self.prevEle = TreeNode(-sys.maxsize - 1)
        
        self.inorderTraversal(root)
        
        #swap the node
        temp = self.firstEle.val
        self.firstEle.val = self.secondEle.val
        self.secondEle.val = temp
