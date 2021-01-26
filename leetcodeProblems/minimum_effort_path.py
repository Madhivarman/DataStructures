from heapq import heappush, heappop

class Solution:
    def minimumEffortPath(self, heights) -> int:
        grid = heights
        # edge cases:
        if not grid:
            return 0
        
        from heapq import heappush, heappop
        h = [(0, (0,0))] # key to heap is cost
        costSoFar = {(0,0): 0} # also serves as a more nuanced visited set

        dirs = [(1,0), (0,1), (-1,0), (0,-1)] # all 4 dirs
        trgt = (len(grid)-1, len(grid[0])-1) # Dijkstra can have early termination condition

        while h:
            cost, node = heappop(h)
            x, y = node
            if node == trgt:
                break
            for dir in dirs:
                newX, newY = x+dir[0], y+dir[1]
                # boundries
                if newX >= 0 and newX <= len(grid)-1 and newY >= 0 and newY <= len(grid[0])-1:
                    edgeCost = max(cost, abs(grid[x][y] - grid[newX][newY])) # -- See [Comment I] below
                    # if nei not seen before or seen before but now revisiting via less costly route
                    if (newX, newY) not in costSoFar or ( (newX, newY) in costSoFar and edgeCost < costSoFar[(newX, newY)]):
                        costSoFar[(newX, newY)] = edgeCost
                        heappush(h, (edgeCost, (newX, newY)))
                        
        return costSoFar[trgt]


tc1 = [[1,2,2],[3,8,2],[5,3,5]]
tc2 = [[1,2,3],[3,8,4],[5,3,5]]
tc3 = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]

print(Solution().minimumEffortPath(tc1))
print(Solution().minimumEffortPath(tc2))
print(Solution().minimumEffortPath(tc3))