"""
    In a given grid, each cell can have one of three values:

    the value 0 representing an empty cell;
    the value 1 representing a fresh orange;
    the value 2 representing a rotten orange.

Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.
"""

from collections import deque

class Solution():    
    def orangesRotting(self, grid):
        totalmins = 0
        row, col = len(grid), len(grid[0])
        visited = [[False for _  in range(col)] for _ in range(row)]
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        q = deque() #to iterate like BFS

        rotten_count, empty_count = 0, 0

        #find where all cell state 2 is present
        for r in range(row):
            for c in range(col):
                if(grid[r][c] == 2):
                    q.append([r, c, 0])
                    visited[r][c] = True
                    rotten_count += 1
                if(grid[r][c] == 0):
                    visited[r][c] = True
                    empty_count += 1
        
        while(q):
            r, c, totalmins = q.popleft()

            for dx, dy in directions:
                nr, nc = r + dx, c + dy
                #condition to check if the move is safe
                if(0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1 and not visited[nr][nc]):
                    grid[nr][nc] = 2 #update the cell
                    rotten_count += 1 #increase the rotten count
                    q.append([nr, nc, totalmins+1])
                    visited[nr][nc] = True
            
        if(rotten_count + empty_count == row * col):
            return totalmins
        
        return -1



grid = [[2,1,1],[1,1,0],[0,1,1]]
grid2 = [[1,1,1],[0,2,2],[1,1,0]]
grid3 = [[2,2,0]]
grid4 = [[2,2,1]]

print(Solution().orangesRotting(grid))
print(Solution().orangesRotting(grid2))
print(Solution().orangesRotting(grid3))
print(Solution().orangesRotting(grid4))