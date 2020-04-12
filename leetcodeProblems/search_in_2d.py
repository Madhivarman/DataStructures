"""
    Problem Statement:
        Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
        Integers in each row are sorted from left to right.
        The first integer of each row is greater than the last integer of the previous row.
"""

class Solution():

    def isPresent(self, matrix, target):
        bool_ = False
        for row in range(len(matrix)):
            low, high = matrix[row][0], matrix[row][-1]
            #it should present within this range
            if low <= target and target <= high:
                if target in matrix[row]:
                    bool_ = True
                    return bool_

        return bool_



tc1 = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
tc1_target = 3

tc2 = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
tc2_target = 13

print(Solution().isPresent(tc1, tc1_target))
print(Solution().isPresent(tc2, tc2_target))