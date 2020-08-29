"""
  Problem Statement:
      Given a set of intervals, for each of the interval i, check if there exists an interval j whose start point is bigger than or equal to 
      the end point of the interval i, which can be called that j is on the "right" of i.

      For any interval i, you need to store the minimum interval j's index, which means that the interval j has the minimum start 
      point to build the "right" relationship for interval i. If the interval j doesn't exist, store -1 for the interval i. Finally, you need 
      output the stored value of each interval as an array.

      Note:
      You may assume the interval's end point is always bigger than its start point.
      You may assume none of these intervals have the same start point.
"""

class Solution:
    def findRightInterval(self, itrs: List[List[int]]) -> List[int]:
        ans = [-1]*len(itrs)
        
        #sort by start time
        itrs_ = sorted([[itr, i] for i,itr in enumerate(itrs)], key = lambda x:x[0])
        
        import heapq
        minHeap = []
        
        for itr,idx in itrs_:
            while minHeap and minHeap[0][0] <= itr[0]: 
                top = heapq.heappop(minHeap)
                ans[top[1]] = idx
            heapq.heappush(minHeap, [itr[1], idx]) # push only end time and idx into the minHeap
        return ans
