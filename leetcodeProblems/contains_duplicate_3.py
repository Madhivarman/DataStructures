"""
    Problem Statement:
      Given an array of integers, find out whether there are two distinct indices i and j 
      in the array such that the absolute difference between nums[i] and nums[j] is at most t 
      and the absolute difference between i and j is at most k.
"""

class Problem:
  def containsNearbyDuplicates(self, arr, k, t):
      
      if len(arr) == 0 and len(set(nums)) == len(nums):
          return False
      
      for i in range(len(arr)):
        #iterate through the k+1
        for j in range(i+k+1, len(arr)):
            if abs(arr[j] - arr[i]) <= t:
              return True
      
      return False
