"""
  Problem Statement:
    You are given an integer n. An array nums of length n + 1 is generated in the following way:

    nums[0] = 0
    nums[1] = 1
    nums[2 * i] = nums[i] when 2 <= 2 * i <= n
    nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n
    Return the maximum integer in the array nums
"""
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if  n == 0:
            return 0
        
        if n == 1 or n == 2:
            return 1
        
        idx = 1
        mx = 0
        nums = [0] *(n+1)
        nums[1] = 1
        
        while(2*idx+1) < n+1:
            nums[2*idx] = nums[idx]
            nums[2*idx+1] = nums[idx] + nums[idx+1]
            mx = max(mx, nums[2*idx], nums[2*idx+1])
            idx += 1
        
        return mx
