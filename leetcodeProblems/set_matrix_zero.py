"""
    Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
    Follow ups:
        A straight forward solution using O(mn) space is probably a bad idea.
        A simple improvement uses O(m + n) space, but still not the best solution.
        Could you devise a constant space solution?
"""
class Solution():

    def setMatrixZero(self, matrix):          
        row = set()
        col = set()

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                  row.add(r)
                  col.add(c)
        
        for r in row:
            matrix[r] = [0] * len(matrix[0])

        for c in col:
            for r in range(len(matrix)):
                matrix[r][c] = 0

        return matrix

tc1 = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
print(Solution().setMatrixZero(tc1))