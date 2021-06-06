import heapq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        #using heapq
        heap = []
        
        for num in nums:
            heapq.heappush(heap, num)
        
        result = 1
        temp = 1
        prev = heapq.heappop(heap)
        
        while heap:
            curr_ele = heapq.heappop(heap)
            diff = curr_ele - prev
            if diff == 1:
                temp += 1
            elif diff == 0:
                continue
            else:
                temp = 1
            
            result = max(result, temp)
            prev = curr_ele
        
        return result
