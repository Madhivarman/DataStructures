"""
  Problem Statement:
    You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score 
    you get by erasing the subarray is equal to the sum of its elements.
    
    Return the maximum score you can get by erasing exactly one subarray.

    An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).
"""
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        result = 0
        seen = set()
        current_sum = 0
        begin_with = 0
        
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i]) #include
                current_sum += nums[i]
                continue
            
            result = max(result, current_sum)
            
            #check where to begin
            while nums[begin_with] != nums[i]:
                current_sum -= nums[begin_with]
                seen.remove(nums[begin_with])
                begin_with += 1 #increment
            
            begin_with += 1
        
        return max(result, current_sum)
