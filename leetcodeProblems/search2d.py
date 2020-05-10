"""
  Problem Statement:
    Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.
"""

class Solution:
    def searchMatrix(self, matrix, target):
        if(len(matrix) == 0):
            return False
        
        row = len(matrix)
        col = len(matrix[0])
        
        i, j = 0, col - 1
        
        while((i >= 0 and i < row) and (j >=0 and j < col)):
            if(matrix[i][j] == target):return True
              
            if(matrix[i][j] > target):
                j -= 1 #left direction
              
            if(matrix[i][j] < target):
                i += 1 #down direction
        
        return False

matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 5

print(Solution().searchMatrix(matrix, target))
