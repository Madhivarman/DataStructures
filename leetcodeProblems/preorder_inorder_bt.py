"""
    Problem Statement:
      Given preorder and inorder traversal of a tree, construct the binary tree.

    Note:
    You may assume that duplicates do not exist in the tree.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution():

    def buildTree(self, preorder, inorder, start, end):

        if start > end:
            return None

        #we know first element of the preorder is Root
        #so, construct a rooot
        root = TreeNode(preorder[self.preindex])
        self.preindex += 1 #increment

        if root is None:
            return None
          
        if start == end:
            return root

        #now we need to find the left and right element
        #in Inorder traversal, the traverse path is left, root, right
        #so, we get the index value from the inorder, then left subtree 
        #would be inorder[:index - 1], right subtree would be inorder[index+1:]
        index = self.inorder_hashmap[root.val]


        #traversal
        root.left = self.buildTree(preorder, inorder, start, index - 1)
        root.right = self.buildTree(preorder, inorder, index + 1, end)

        return root

    def formBinaryTree(self, preorder, inorder):
        #preorder -> Root, Left, Right
        #inorder -> Left, root, Right
        #postorder -> Left, Right, Root

        self.inorder_hashmap = {}
        self.preindex = 0

        for num, i in enumerate(inorder):
          self.inorder_hashmap[i] = num
        
        return self.buildTree(preorder, inorder, 0, len(inorder)-1)