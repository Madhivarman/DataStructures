"""
    Problem Statement:
        On a 2-dimensional grid, there are 4 types of squares:

        1 represents the starting square.  There is exactly one starting square.
        2 represents the ending square.  There is exactly one ending square.
        0 represents empty squares we can walk over.
        -1 represents obstacles that we cannot walk over.
        Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.
"""

from collections import deque

class Solution():

    def uniquePath(self, grid):
        self.unique_path = 0
        total_cell = 0

        start_square = 0

        def dfs(coords, rest_):
            x, y = coords[0], coords[1]
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] < 0:
                return

            if grid[x][y] == 2 and rest_ == 0:
                self.unique_path += 1
            
            neighbors = [[0, 1],[0,-1],[1,0],[-1,0]]

            for nx, ny in neighbors:
                save = grid[x][y]
                grid[x][y] = -2                
                dfs((x+nx, y+ny), rest_ - 1)
                grid[x][y] = save

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    start_square = (i, j)
                
                if grid[i][j] != -1:
                    total_cell += 1

        dfs(start_square, total_cell - 1)
        return self.unique_path

        

tc1 = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
tc2 = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
tc3 = [[0,1],[2,0]]

print(Solution().uniquePath(tc1))
print(Solution().uniquePath(tc2))
print(Solution().uniquePath(tc3))