"""
  PROBLEM STATEMENT:
    Suppose you have n integers from 1 to n. We define a beautiful arrangement as an array that is constructed by these n 
    numbers successfully if one of the following is true for the ith position (1 <= i <= n) in this array:

    The number at the ith position is divisible by i.
    i is divisible by the number at the ith position.
    Given an integer n, return the number of the beautiful arrangements that you can construct.
"""
0class Solution:
    
    def swap(self, nums, i, j):
        if i == j:
            return
        
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
    
    def dfs(self, nums, index):
        #break condition
        if index == len(nums):
            self.ans += 1
            return
        
        for j in range(index, len(nums)):
            if (index % nums[j] == 0) or (nums[j] % index == 0):
                self.swap(nums, index, j)
                self.dfs(nums, index+1)
                self.swap(nums, j, index)
        
    def countArrangement(self, n: int) -> int:
        self.ans = 0
        nums = [x for x in range(0, n+1)]
        self.dfs(nums, 1)
        return self.ans
