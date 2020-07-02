"""
  Problem Statement:
  There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], 
  and the cost of flying the i-th person to city B is costs[i][1].
  Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.
"""
from queue import PriorityQueue

class Solution:
    def twoCitySchedCost(self, costs):
        q = PriorityQueue()
        totalcost = 0
        
        for ca, cb in costs:
            diff = (ca - cb)
            q.put((diff, (ca, cb)))
        
        ca, cb = 0, 0
        
        sorted_array = []
        
        while not q.empty():
            diff, (ca, cb) = (q.get())
            #print(diff, ca, cb)
            sorted_array.append([ca, cb])
        
        n = len(sorted_array) // 2
        p = 0
        
        #print(sorted_array)
        
        for a, b in sorted_array:
            if p < n: 
                totalcost += a
            else:
                totalcost += b
            
            p += 1
        
        return totalcost
