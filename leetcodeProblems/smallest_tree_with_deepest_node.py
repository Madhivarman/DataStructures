"""
  Problem Statement:
    Given a binary tree rooted at root, the depth of each node is the shortest distance to the root.

    A node is deepest if it has the largest depth possible among any node in the entire tree.

    The subtree of a node is that node, plus the set of all descendants of that node.

    Return the node with the largest depth such that it contains all the deepest nodes in its subtree.
"""

class Solution:
    def helperUtil(self, tree):
        if tree is None:
            return 0, None
        
        left = self.helperUtil(tree.left)
        right = self.helperUtil(tree.right)
        
        if left[0] > right[0]:
            return left[0] + 1, left[1]
        
        elif left[0] < right[0]:
            return right[0]+1, right[1]
        
        else:
            return left[0]+1, tree
        
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        return self.helperUtil(root)[1]
