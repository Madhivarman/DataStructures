"""
    Problem Statement:
        Given an array nums, write a function to move all 0's to the end of it while maintaining the 
        relative order of the non-zero elements.
"""

class Solution():
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0 
        for i, val in enumerate(nums):
            if val != 0:
                nums[count] = val
                count += 1
        
        while(count < len(nums)):
            nums[count] = 0
            count += 1 #increment the count
        
        return nums


tc1 = [0,1,12,3,4,5,0,0,9,10, 12]
print(Solution().moveZeroes(tc1))