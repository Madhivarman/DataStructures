"""
    Given an array of integers and an integer k, you need to find the
    total number of continuous subarrays whose sum equals to k.
"""

class Solution():
    def findCountSubArrayEqualsK(self, nums, target):
        count = 0 
        s = 0 #cumulative count
        dict_ = {0:1} #to store the values

        for num in nums:
            s += num #cumulative value

            if s - target in dict_:
                count += dict_[s]

            if s not in dict_:
                dict_[s] = 1 #initialize
            else:
                dict_[s] += 1 #increment the count                

        return count


nums = [-1,2,-2,-3,3,-4,5,6,7,8,-2]
target = 0

print(Solution().findCountSubArrayEqualsK(nums, target))
