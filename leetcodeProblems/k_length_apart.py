"""
    Problem Statement:
        Given an array nums of 0s and 1s and an integer k, return True if all 1's are at least k places away from each other, otherwise return False
"""
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        idx_map = {}
        
        if 1 not in nums:
            return True
        
        for idx, val in enumerate(nums):
            if val not in idx_map:
                idx_map[val] = [idx]
            else:
                idx_map[val].append(idx)
        
        places = idx_map[1]
        prev = places[0]
        
        idx = 1
        
        #print(places)
        
        while(idx < len(places)):
            diff = places[idx] - prev
            if diff <= k:
                return False
            prev = places[idx] #update
            idx += 1
        
        return True
