"""
  Problem Statement:
    We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
    (Here, the distance between two points on a plane is the Euclidean distance.)
    You may return the answer in any order.  The answer is guaranteed to be unique 
    (except for the order that it is in.)
"""

class Solution():
      def kClosest(self, points, K):
        #using max heap to get the K closest point
        #using eucledian formula to calculate distance
        heap = []
        (x1, y1) = (0,0)
        
        #iterate through the coordinates
        #formulate sqrt((x2-x1)^2 + (y2-y2^2))
        for x2, y2 in points:
            d = (x2 - x1)**2 + (y2 - y1) ** 2
            distance = math.sqrt(d)
            #append to the heap
            heapq.heappush(heap, (distance, [x2, y2]))
        
        index = 0
        result = []
        
        while(index < K):
            val, coordinates = heapq.heappop(heap)
            result.append(coordinates)
            index += 1
        
        return result
        
points = [[1,3],[-2,2]]
K = 1

print(Solution().kClosest(points, K))
