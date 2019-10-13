class TreeNode:
    def __init__(self, x):
          self.val = x
          self.left = None
          self.right = None


def convertBST(self, root: TreeNode) -> TreeNode:
        self.sum = 0
        
        def afterOrder(cur):
            
            if cur == None:
                return
            
            #start traversing through right
            afterOrder(cur.right)
            
            #once its null, update sum and node val
            self.sum += cur.val
            cur.val = self.sum
            
            #once entire subtree is finished traverse left
            #sub tree
            afterOrder(cur.left)
            
        afterOrder(root)
        
        return root
 
 #follows same structure as before to create tree
 
 sol = convertBST(root)
