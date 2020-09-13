"""
    Problem Statement:
            Serialization is the process of converting a data structure or object into a sequence of bits 
            so that it can be stored in a file or memory buffer, or transmitted across a network connection link to 
            be reconstructed later in the same or another computer environment.

            Design an algorithm to serialize and deserialize a binary tree. There is no restriction 
            on how your serialization/deserialization algorithm should work. You just need to ensure that a 
            binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
"""
from collections import deque

#Tree Template
class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution():
    def serialize(self, root):
        if root is None:
            return []

        data = []
        q = deque([])
        q.append((root))

        while q:
            currnode = q.popleft()
            if currnode:
                data.append(currnode.val)
                q.append(currnode.left)
                q.append(currnode.right)
            else:
                data.append("#")

        return data 
    
    def deserialize(self, data):
        if not data:
            return []

        q = deque([])
        root = TreeNode(data[0])
        q.append((root))
        idx = 1

        while q and idx >= len(data):
            currnode = q.popleft()

            if data[idx] != '#':
                left = TreeNode(data[idx])
                currnode.left = left
                q.append(left)
            
            idx  += 1

            if idx >= len(data):
                break

            if data[idx] != '#':
                right = TreeNode(data[idx])
                currnode.right = right
                q.append(right)
            
            idx += 1

        return root