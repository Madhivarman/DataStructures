"""
  Problem Statement:
    Given a list of non-negative numbers and a target integer k, write a function to check if the array has
    a continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where
    n is also an integer.
"""
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        #base condition - 1
        if len(nums) < 2:
            return False
        
        #base condition - 2
        if k == 0:
            for i in range(len(nums) - 1):
                if nums[i] == 0 and nums[i+1] == 0:
                    return True
            
            return False
        
        for i in range(len(nums)-1):
            total = nums[i] + nums[i+1]
            
            if (nums[i] + nums[i+1]) % k == 0:
                return True
            
            for j in range(i+2, len(nums)):
                total += nums[j]
                if total % k == 0:
                    return True
        
        return False
