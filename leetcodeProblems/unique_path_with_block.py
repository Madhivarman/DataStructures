class Solution():

    #this solution passed all the m x n test cases
    #where n > 1
    def uniquePath(self, grid):
        row, col = 0 ,0

        #there is no way that robot can move
        if grid[row][col+1] == 1 and grid[row+1][col] == 1:
            return 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if i == 0 and j == 0:
                    grid[i][j] = 1 

                #if block is there, then change it to 
                #zero, because the path cannot be made from there
                elif grid[i][j] == 1:
                    grid[i][j] = 0
                else:
                    #get the current cell left and up position
                    left, up = [i, j-1], [i-1,j]
                    if up[0] == -1:
                        grid[i][j] = grid[left[0]][left[1]] + 0
                    elif left[0] == -1:
                        grid[i][j] = 0 + grid[up[0]][up[1]]
                    else:
                        grid[i][j] = grid[left[0]][left[1]] + grid[up[0]][up[1]]
        
        return grid[len(grid)-1][len(grid)-1]


tc1 = [[0,0,0,0,0,1],[1,0,0,0,0,0],[0,0,1,0,1,0],[0,0,0,0,0,0],[0,1,0,1,0,0],[1,0,0,0,0,0]]
tc2 = [[0,0,0],[0,1,0],[0,0,0]]

print(Solution().uniquePath(tc1))
print(Solution().uniquePath(tc2))