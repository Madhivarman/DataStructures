"""
  Problem Statement:
      Given an array of integers nums and a positive integer k, find whether it's possible to divide this array 
      into k non-empty subsets whose sums are all equal.
"""

class Solution:
    
    def dfs(self, partitions, t, nums):
        #if the array is empty return True
        if not nums:
            return True
        
        #pop the last number
        v = nums.pop()
        
        for i, val in enumerate(partitions):
            if val + v <= t:
                partitions[i] += v #add the sum
                #recursive call
                if(self.dfs(partitions, t, nums)):
                    return True
                
                #backtrack
                partitions[i] -= v
                if not val:
                    break
        
        nums.append(v) #append the val to the list
        
        return False

    def canPartitionKSubsets(self, nums, k):
        #check
        if(len(nums) == 0 or sum(nums)%k):
            return False
        
        t = sum(nums) / k #subset sum
        partitions = [0] * k
        
        nums.sort() #sort the array list 
        
        if nums[-1] > t:
            return False
        
        return self.dfs(partitions, t, nums)


tc1, tc1_k = [4, 3, 2, 3, 5, 2, 1], 4 
tc2, tc2_k = [1, 1, 3, 2, 2], 4
tc3, tc3_k = [10,10,10,7,7,7,7,7,7,6,6,6], 3

print(Solution().canPartitionKSubsets(tc1, tc1_k))
print(Solution().canPartitionKSubsets(tc2, tc2_k))
print(Solution().canPartitionKSubsets(tc3, tc3_k))
