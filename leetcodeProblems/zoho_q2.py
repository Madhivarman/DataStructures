"""
    Problem Statement:
        Write a program to traverse an array from left to right and replace each number with
        the first number greater than the current one from the remaining elements from the
        current position. For example, from (4, 9, 23, 7) the next greater number to 4 is 7. If
        no such number is found, then set the current and the remaining array elements as -1.
"""

class Solution():
    def replaceGreaterNumber(self, nums):
        result = [-1] * len(nums)
        idx = 0

        while(idx < len(nums)-1):
            to_traverse = nums[idx+1:]
            all_greater = []
            for t in to_traverse:
                if nums[idx] < t:
                    all_greater.append(t)
            
            result[idx] = min(all_greater) if len(all_greater) != 0 else -1
            idx += 1 #update

        return result

tc1 = [2,5,7]
tc2 = [2,4,8,90,77,54]
tc3 = [2,-1,0,-1,3]

print(Solution().replaceGreaterNumber(tc1))
print(Solution().replaceGreaterNumber(tc2))
print(Solution().replaceGreaterNumber(tc3))