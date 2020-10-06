"""
  Problem Statement:
  You are given the root node of a binary search tree (BST) and a value to insert into the tree. 
  Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

  Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. 
  You can return any of them.
"""
class Solution:        
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def dfs(root):
            if val < root.val:
                if root.left:
                    dfs(root.left)
                else:
                    root.left = TreeNode(val)
            else:
                if root.right:
                    dfs(root.right)
                else:
                    root.right = TreeNode(val)
        
        if not root: 
            return TreeNode(val)
        
        dfs(root)
        return root
