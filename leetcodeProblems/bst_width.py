"""
    Problem Statement:
        Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the 
        maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes 
        are null.

        The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null
        nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.
"""

from collections import deque

class Solution():
    def bstWidth(self, tree):
        width = 0

        if tree is None:
            return 0
        
        q = deque([])
        q.append([(tree, 0)]) #append the root val, params = (tree, index)

        next_level = deque([])

        while q:
            curr_tree, index = q.popleft()
            #left tree index calculation 2 * i
            if curr_tree.left:
                next_level.append([(curr_tree.left, index * 2)])
            
            #right tree index calculation 2 * i + 1
            if curr_tree.right:
                next_level.append([(curr_tree.right, index * 2 +1)])
            
            if len(q) == 0 and next_level:
                width = max(width, next_level[-1][1] - next_level[0][1] + 1)
                q, next_level = next_level, q
        
        return width

        
