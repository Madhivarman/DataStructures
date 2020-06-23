"""
   Problem Statement:
        Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
"""

from queue import PriorityQueue

class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    
    def helperUtil(self, pq, lst, rst):
        if lst is not None:
            pq.put(- lst.val)
            self.helperUtil(pq, lst.left, lst.right)
        
        if rst is not None:
            pq.put(- rst.val)
            self.helperUtil(pq, rst.left, rst.right)
        
        return pq
        
    def kthSmallest(self, root, k):
        pq = PriorityQueue()
        pq.put(-root.val)
        pq = self.helperUtil(pq, root.left, root.right)
        
        result = []
        
        while not pq.empty():
            result.append(abs(pq.get()))
        
        return result[-k]
