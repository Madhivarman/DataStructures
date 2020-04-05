"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.
"""

class Solution:

    def canJump(self, nums):
        #hack found it from the solution
        length = len(nums)
        i, maximum = 0, 0
        
        if len(nums) == 1:
            return True
        
        while(i <= maximum):
            maximum = max(maximum, i+nums[i])
            if maximum >= length - 1:
                return True
            
            i += 1 #increment the pointer loop
        
        return False


tc1 = [2,3,1,1,4]
tc2 = [3,2,1,0,4]
#tc3 = []
tc4 = [2, 0]
tc5 = [2, 5, 0, 0]


print(Solution().canJump(tc1))
print(Solution().canJump(tc2))
print(Solution().canJump(tc4))
print(Solution().canJump(tc5))