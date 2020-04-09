"""
    Problem statement:
        A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
        The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
        How many possible unique paths are there?
"""

#wont work in large cases
class Solution():

    def __init__(self, m, n):
        self.col = m
        self.row = n
        self.grid = [[False]*self.col for _ in range(self.row)]
        self.direction = [(0,1),(1,0)]
        self.path = 0
    
    def canReach(self, r, c):

        if self.grid[r][c] == 'E':
            self.path += 1
            return
        
        for dx, dy in self.direction:
            cr, cc = r+dx, c+dy
            if 0 <= cr < self.row and 0 <= cc < self.col:
                self.canReach(cr, cc)

        return self.path

    def uniquePaths(self):
        #set the robot and star
        self.grid[0][0] = 'S'
        self.grid[self.row-1][self.col-1] = 'E'

        #initial value
        unique_path = 0

        r, c = 0, 0 

        return self.canReach(r, c)



class DP():
    def uniquePaths(self, m, n):
        grid = [[1]*n for _ in range(m)]
        
        for i in range(len(grid)-1):
            for j in range(1, len(grid[0])):
                grid[i+1][j] = grid[i][j] + grid[i+1][j-1]
        
        return grid[m-1][n-1]


print(DP().uniquePaths(3, 2))
print(DP().uniquePaths(7, 3))
print(DP().uniquePaths(5, 3))
print(DP().uniquePaths(27, 52))
print(DP().uniquePaths(100, 100))