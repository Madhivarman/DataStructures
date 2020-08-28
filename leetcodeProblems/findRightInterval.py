class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        ans = [-1]*len(intervals)
        
        itrs_ = sorted([[itr, i] for i,itr in enumerate(intervals)], key = lambda x:x[0]) #sort by start time
        
        import heapq
        minHeap = []
        
        for itr,idx in itrs_:
            while minHeap and minHeap[0][0] <= itr[0]: 
                top = heapq.heappop(minHeap)
                ans[top[1]] = idx
            heapq.heappush(minHeap, [itr[1], idx]) # push only end time and idx into the minHeap
        return ans
