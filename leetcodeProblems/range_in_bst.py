class Solution:
    
    def helperUtil(self, lst, rst, L, R):   
        if lst is not None:
            if lst.val >= L and lst.val <= R:
                self.result += lst.val
            
            self.helperUtil(lst.left, lst.right, L, R)
        
        if rst is not None:
            if rst.val >= L and rst.val <= R:
                self.result += rst.val
            
            self.helperUtil(rst.left, rst.right, L, R)
        
        return self.result
    
    def rangeSumBST(self, root, L, R):
        
        if root is None:
            return 0
        
        lst = root.left
        rst = root.right
        
        if root.val >= L and root.val <= R:
            self.result = root.val
        else:
            self.result = 0
        
        return self.helperUtil(lst, rst, L, R) 
