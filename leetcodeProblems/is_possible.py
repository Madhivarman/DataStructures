"""
  Problem Statement:
    Given an array of integers target. From a starting array, A consisting of all 1's, you may perform the following procedure :
    let x be the sum of all elements currently in your array.
    choose index i, such that 0 <= i < target.size and set the value of A at index i to x.
    You may repeat this procedure as many times as needed.
    Return True if it is possible to construct the target array from A otherwise return False.
"""

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        #bottom up approach
        if len(target) == 1:
            return target[0] == 1
        
        q = [-x for x in target]
        heapq.heapify(q)
        
        while q:
            total = -sum(q)
            curr_max = -heapq.heappop(q)
            if curr_max == 1:
                return True
            if curr_max < 1 or 2 * curr_max <= total or curr_max == total:
                return False
            prev = curr_max % (total-curr_max)
            heapq.heappush(q, -prev)
