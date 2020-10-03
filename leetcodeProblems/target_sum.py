"""
  Problem Statement:
    You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. 
    For each integer, you should choose one from + and - as its new symbol.

    Find out how many ways to assign symbols to make sum of integers equal to target S.
"""

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        memoization = {}
        
        def dfs(idx, val):            
            if (idx, val) in memoization:
                return memoization[(idx, val)]
            
            if idx == len(nums):
                if val == S:
                    return 1
                return 0
            
            memoization[(idx, val)] = dfs(idx + 1, val + nums[idx]) + dfs(idx+1, val - nums[idx])
            
            return memoization[(idx, val)]

        ways = dfs(0,0)
        return ways
