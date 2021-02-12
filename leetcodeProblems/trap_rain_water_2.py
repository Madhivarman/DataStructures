"""
    Problem Statement:
        Given an m x n matrix of positive integers representing the height of each unit cell
        in a 2D elevation map, compute the volume of water it is able to trap after raining.
"""
from heapq import heappush, heappop

class Solution():
    def trapWater(self, heightMap):
        h=[]
        row_l=len(heightMap)
        col_l=len(heightMap[0])
        
        visited=set()
        
        for i in range(row_l):
            heappush(h,(heightMap[i][0],i,0))
            heappush(h,(heightMap[i][col_l-1],i,col_l-1))
            visited.add((i,0))
            visited.add((i,col_l-1))
        # print(visited)    
        for j in range(col_l):
            heappush(h,(heightMap[0][j],0,j))
            heappush(h,(heightMap[row_l-1][j],row_l-1,j))
            visited.add((0,j))
            visited.add((row_l-1,j))
            
        # print(visited)
        
        total=0
        maxi=float('-inf')
        while len(h)>0:
            height,row,col=heappop(h)
            
            maxi=max(maxi,height)
            
            
            for dir in [(1,0),(-1,0),(0,-1),(0,1)]:
                row1=row+dir[0]
                col1=col+dir[1]
                
                if 0<=row1<row_l and 0<=col1<col_l and (row1,col1) not in visited:
                    if maxi>heightMap[row1][col1]:
                        total+=(maxi-heightMap[row1][col1])
                    heappush(h,(heightMap[row1][col1],row1,col1))
                    visited.add((row1,col1))
                    
        return total 

tc1 = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
tc2 = [[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]

print(Solution().trapWater(tc1))
print(Solution().trapWater(tc2))
