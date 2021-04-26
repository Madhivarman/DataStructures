"""
  Problem Statement;
    You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

    You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

    While moving from building i to building i+1 (0-indexed),

    If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
    If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
    Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.
"""

class Solution():
  def farthestBuildingReach(self, heights, bricks, ladders):
    min_heap= []
    
    for i in range(len(heights)-1):
      height_diff = heights[i+1] - heights[i]
      
      if height_diff > 0:
        heapq.heappush(min_heap, height_diff)
        
        if len(min_heap) > ladders:
          top_bricks = heapq.heappop(min_heap)
          bricks -= top_bricks
        
        if bricks < 0:
          return i
    
    return len(heights) - 1
