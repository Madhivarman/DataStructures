"""
	Given a non-empty array of integers, return the k most frequent elements.
"""

from collections import OrderedDict

class Solution:
    def topKFrequent(self, nums, k):
        hashmap = {}
        
        #safe check
        if(len(nums) == 0):
            return 
        
        #creates an hashmap
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        
        #K most frequent elements
        #sort by values
        sorted_x = sorted(hashmap.items(), key=lambda x: x[1])
        sorted_x = OrderedDict(sorted_x)
        sorted_x = collections.OrderedDict(reversed(list(sorted_x.items()))) #desc order
        
        output = []
        
        round_ = 1
        
        for key, v in sorted_x.items():
            if round_ > k:
                return output
            
            output.append(key)
            round_ += 1
        
        return output
		
array = [1,1,1,2,2,3]
k = 1
print(Solution().topKFrequent(array, k))
