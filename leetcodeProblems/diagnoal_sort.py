"""
  Problem Statement:
      A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in 
      the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, 
      includes cells mat[2][0], mat[3][1], and mat[4][2].

      Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.
"""
class Solution:
    
    def getCells(self, r, c, mat, values, cells):
        directions = [[1,1]]
        values.append(mat[r][c])
        cells.append((r, c))
        
        for dx, dy in directions:
            nr, nc = r + dx, c + dy
            #boundary check
            if 0 <= nr < len(self.result) and 0 <= nc < len(self.result[0]) and self.result[nr][nc] == 0:
                self.getCells(nr, nc, mat, values, cells)
            
        return values, cells
    
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        self.result = [[0 for x in range(col)] for _ in range(row)]
        hashmap = {} #to store idx, and val
        
        #start with idx 0,0 fill the matrix
        for i in range(row):
            for j in range(col):
                if self.result[i][j] == 0:
                    vals, cells = self.getCells(i, j, mat,[],[])
                    #sort the vals
                    sv = sorted(vals)
                    for v, cell in zip(sv, cells):
                        ridx, cidx = cell[0], cell[1]
                        self.result[ridx][cidx] = v 
        
        return self.result
