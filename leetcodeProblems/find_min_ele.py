"""
  Problem Statement:
    Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
    (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
    Find the minimum element.
    The array may contain duplicates.
"""
import heapq

class Solution:
    def findMin(self, nums):
        q = []
        for num in nums:
            heapq.heappush(q, num)
        
        element = heapq.heappop(q)
        return element
