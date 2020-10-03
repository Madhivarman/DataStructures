"""
  Problem Statement:
    Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

    A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:
      0 <= i, j < nums.length
      i != j
      a <= b
      b - a == k
"""

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        idx = 0
        pairs = {}
        total_pairs = 0
        
        nums.sort(reverse=True)
        
        while(idx < len(nums)):
            diff = nums[idx] - k
            insearch = nums[:idx] + nums[idx+1:]
            
            if diff in insearch:
                if ((nums[idx], diff)) in pairs:
                    pairs[(nums[idx], diff)] += 1
                    pairs[(diff, nums[idx])] += 1
                else:
                    pairs[(nums[idx], diff)] = 1 
                    pairs[(diff, nums[idx])] = 1
                    
                    total_pairs += 1 #increment the total pairs
            
            idx += 1 #increment
        
        
        return total_pairs
