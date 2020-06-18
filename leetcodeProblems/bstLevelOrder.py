"""
    Problem Statement:
        Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
        For example:
        Given binary tree [3,9,20,null,null,15,7],
        Result:
            [[3],[9,20],[15,7]]
"""

class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:     
    
    def helperUtil(self, lst, rst, result, level):
        #to add layer to the stack
        if len(result) < level:
            result.append([])
        
        #keep checking left sub tree
        if lst is not None:
            result[level-1].extend([lst.val])
            self.helperUtil(lst.left, lst.right, result, level+1)
        
        #keep tracking right sub tree
        if rst is not None:
            result[level-1].extend([rst.val])
            self.helperUtil(rst.left, rst.right, result, level+1)
        
        return result
        
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        #if tree is empty
        if root is None:
            return []
        
        result = [[root.val]]
        lst = root.left
        rst = root.right
        
        result = self.helperUtil(lst, rst, result, 2)
        
        result = [x for x in result if len(x) != 0]
        
        return result
