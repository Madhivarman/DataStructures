from collections import deque

class Solution:
    
    #using BFS
    def helperUtil(self, matrix, r, c, dist):
        directions = [[0,1],[0,-1],[-1,0],[1,0]]
        q = deque()
        q.append([r, c, dist])
        
        while q:
            dr, dc, dist = q.popleft()
            
            for dx, dy in directions:
                nr, nc = dr + dx, dc + dy
                
                if 0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]):
                    if matrix[nr][nc] == 0:
                        return dist + 1
                
                    q.append((nr, nc, dist+1))
        
        return dist + 1

            
    def updateMatrix(self, matrix):
        #row,col
        row, col = len(matrix), len(matrix[0])
        
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    pass
                else:
                    matrix[r][c] = self.helperUtil(matrix, r, c, 0)
        
        return matrix

tc1 = [[0,0,0],[0,1,0],[0,0,0]]
print(Solution().updateMatrix(tc1))
