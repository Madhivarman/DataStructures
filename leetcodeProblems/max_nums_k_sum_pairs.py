"""
  Problem Statement:
      You are given an integer array nums and an integer k.

      In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

      Return the maximum number of operations you can perform on the array.
"""
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        #sort
        nums = sorted(nums)
        i,j = 0, len(nums) - 1
        result = []
        
        
        while (i < j):
            sum_ = nums[i] + nums[j]
            if sum_ < k:
                i += 1
            elif sum_ == k:
                result.append([nums[i], nums[j]])
                i += 1
                j -= 1
            else:
                j -= 1
        
        return len(result)
