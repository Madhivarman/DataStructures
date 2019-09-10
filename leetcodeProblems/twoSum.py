class Solution:
    def twoSum(self, nums, target):
        index_return, twoElement = [], []
        #first loop
        for i in nums:
            #get index for first element
            indexofi = nums.index(i)
            for j in nums[indexofi + 1:]:
                currentsum = i + j
                if currentsum == target:
                    index_return = [nums.index(i), nums.index(j, indexofi+1)]


        return index_return

s = Solution()
indexes = s.twoSum([2, 2, 7, 11, 15], 4)

print(indexes)