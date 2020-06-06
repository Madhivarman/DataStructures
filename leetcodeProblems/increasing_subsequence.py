"""
  Problem Statment:
      Given an integer array, your task is to find all the different possible increasing subsequences of the given array,
      and the length of an increasing subsequence should be at least 2.
"""

class Solution():
    def increasingSubsequence(self, nums):
        def utilFunction(temp, index, sequence):
            #if index reaches the last element
            #return
            if(index == len(nums)):
                #if the temp has more than 2 elements
                if(len(temp) >= 2):
                    sequence.add(sequence)
                return
            
            #recursive call
            utilFunction(temp, index + 1, sequence)
            
            if not temp or temp[-1] <= nums[index]:
                #recursive call
                utilFunction(temp + (nums[index],), index+1, sequence)
        
        sequence = set()
        utilFunction((), 0, sequence) #helper function
        return sequence
        
tc1 = [4, 6, 7, 7]
tc2 = [-10,2,3,-7, 9]
tc3 = [-10,2,3,-7, 9,10, 11, 12, 0, -100]

print(Solution().increasingSubsequence(tc1))
print(Solution().increasingSubsequence(tc2))
print(Solution().increasingSubsequence(tc3))
