"""
    Problem Statement:
        Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
        (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
        You are given a target value to search. If found in the array return true, otherwise return false.
"""

class Solution():
    def isElementPresent(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while(left <= right):
            mid = left + (right - left) // 2
            
            #mid element is the target
            if nums[mid] == target:
                return True
            
            #Check what side of the subarray is linearly increasing
            elif (nums[left] < nums[mid]):
                #if the target lies in that range and left subarray is strictly increasing
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            else:
                if nums[mid] <= target and  nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1

        return False

tc1, tc1_target = [2,5,6,0,0,1,2], 3
tc2, tc2_target = [2,5,6,0,0,1,2], 2

print(Solution().isElementPresent(tc1, tc1_target))
print(Solution().isElementPresent(tc2, tc2_target))