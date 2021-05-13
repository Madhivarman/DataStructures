#TLE Exception
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.nrows = len(self.matrix)
        self.ncols = len(self.matrix[0])
    
    def dfs(self, x, y, direction):
        self.isvisited[x][y] = True #make it as true
        #iterate
        for dx, dy in direction:
            nx,ny = x + dx, y+dy
            #boundary check
            if self.xlow <= nx <= self.xupp and self.ylow <= ny <= self.yupp and self.isvisited[nx][ny] == False:
                self.ans += self.matrix[nx][ny]
                self.isvisited[nx][ny] = True
                self.dfs(nx, ny, direction) #call stack
        return
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        self.isvisited = [[False for _ in range(self.ncols)] for _ in range(self.nrows)]
        self.ans = 0
        self.xlow, self.ylow = row1, col1
        self.xupp, self.yupp = row2, col2
        print(row1, col1, row2, col2)
        #four directions
        #left, right, up, bottom, diagonal
        direction = [[-1, 0],[1,0], [0,1], [0,-1], [1,1]]
        #make copy of the pointer
        x, y = row1,col1
        self.ans = self.matrix[x][y]
        self.isvisited[x][y] = True
        self.dfs(x, y, direction)
        return self.ans
 
#optimized solution
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        # print(matrix)
        self.sums = [[0 for i in range(len(matrix[0])+1)] for i in range(len(matrix)+1)]
        # print(self.sums)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.sums[i+1][j+1] = matrix[i][j] + self.sums[i][j+1] + self.sums[i+1][j] - self.sums[i][j] 
        # print(self.sums)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sums[row2+1][col2+1] - self.sums[row1][col2+1] - self.sums[row2+1][col1] + self.sums[row1][col1]
