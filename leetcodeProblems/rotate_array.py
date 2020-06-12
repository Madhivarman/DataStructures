"""
  Problem Statement:
      Given an array, rotate the array to the right by k steps, where k is non-negative.

      Follow up:

    Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
    Could you do it in-place with O(1) extra space?
"""

class Solution:
    def optimalSol(self, nums, k):
        if len(nums) == k: 
          return nums
        
        if len(nums) < k:
            k =  k % len(nums) 
        
        nums[:] = nums[-k:] + nums[:-k]
        
        
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer = 1
        copy_ = nums.copy()
        while pointer <= k:
            copy_ = [copy_[-1]] + copy_[:len(nums)-1]
            pointer += 1
        
        for num, ele in enumerate(copy_):
            nums[num] = ele
