#File Descriptive - pesudo palindromic path in Binary Tree
"""
  Problem Statement:
    Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be 
    pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

    Return the number of pseudo-palindromic paths going from the root node to leaf nodes.
"""

class TreeNode():
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

class Solution:
    def dfs(self, root, count):
        if not root:
            return
        
        count[root.val] += 1
        
        #iterate till the end of the leaf
        if not root.left and  not root.right:
            self.ans += sum( v%2 for v in count.values()) <= 1
            return
        
        #recursive call
        self.dfs(root.left, copy.deepcopy(count))
        self.dfs(root.right, copy.deepcopy(count))
        
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        self.ans = 0
        self.dfs(root, Counter())
        return self.ans
