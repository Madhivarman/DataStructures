class Solution:
    def longestIncreasingPath(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        
        row, col = len(grid), len(grid[0])
        self.result = 1

        directions = [[-1, 0], [1,0], [0, 1], [0, -1]]

        #helper function
        def dfs(grid, coords, sum_):
            #get the maximum
            self.result = max(self.result, sum_)
            x, y = coords[0], coords[1]
            
            for dx, dy in directions:
                nr, nc = x + dx, y + dy

                #boundar check and condition
                if 0 <= nr < row and 0 <= nc < col and grid[x][y] < grid[nr][nc]:
                    #call stack
                    dfs(grid, (nr, nc), sum_+1)
                

            return self.result

        #from each cell we need to find the what is
        #the longest increasing path
        for i in range(row):
            for j in range(col):
                dfs(grid, (i, j), 1)

        return self.result
