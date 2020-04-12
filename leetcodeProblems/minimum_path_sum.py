"""
    Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
    Note: You can only move either down or right at any point in time.
"""

class Solution():
    def minimumPathSum(self, grid):

        if len(grid)==0:
            return 0

        row=len(grid)
        col=len(grid[0])

        dp=[]
        for k in range(row):
            dp.append([0]*col)

        dp[0][0]=grid[0][0]

        for j in range(1,col):
            dp[0][j]=sum(grid[0][:j+1])
            
        for i in range(1,row):
            dp[i][0]=sum([x[0] for x in grid[:i+1]])

        for i in range(1,row):
            for j in range(1,col):               
                dp[i][j]=min(dp[i][j-1],dp[i-1][j])+grid[i][j]

        return dp[-1][-1]
        
tc1 = [[1,3,1],[1,5,1],[4,2,1]]
print(Solution().minimumPathSum(tc1))