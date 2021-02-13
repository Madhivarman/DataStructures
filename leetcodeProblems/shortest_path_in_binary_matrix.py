"""
  Problem Statement:
      In an N by N square grid, each cell is either empty (0) or blocked (1).

      A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

      Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
      C_1 is at location (0, 0) (ie. has value grid[0][0])
      C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
      If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
      Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.
"""
class Solution:
        
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        #8 directions
        directions = [[1,0],[0,1],[-1,0],[0,-1],
                           [-1,-1],[1,1],[1,-1],[-1,1]]
        
        q = deque([(1,0,0)]) if grid[0][0] == 0 else deque() #(distance, rowidx, colidx)
        visited = set()
        
        while q:
            distance, x, y  = q.popleft()
            
            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                return distance
            
            for dx, dy in directions:
                nr, nc = x + dx, y + dy
                #boundary check
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 0 and (nr,nc) not in visited:
                    visited.add((nr, nc))
                    q.append((distance+1, nr, nc))
        
        return -1
