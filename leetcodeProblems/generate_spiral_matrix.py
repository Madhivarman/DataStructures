"""
 Problem  Statement:
    Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
"""
class Solution:

    def __init__(self):
        self.dr = [0, 1, 0, -1]
        self.dc = [1, 0, -1, 0]


    def generateSpiral(self, n):
        result = []
        matrix = [['-'] * n for _ in range(n) ]

        #row movement => right, down, left ,up
        dr_r = [0, 1, 0, -1]
        #column movement => down, left, up, right
        dr_c = [1, 0, -1, 0]
        row, col = n, n

        ischecked = [[False] * col for _ in range(n)]

        #initial pointer
        r, c, direction = 0, 0, 0

        #iterate through M*N times
        for i in range(1, n*n+1):
            matrix[r][c] = i
            #update the cell as seen
            ischecked[r][c] = True
            
            #get current row and current column
            cr, cc = r + dr_r[direction], c + dr_c[direction]
            
            if 0 <= cr < row and 0 <= cc < col and not ischecked[cr][cc]:
                r,c = cr, cc
            else:
                #4 represents possible movements
                direction = (direction + 1) % 4
                r, c = r + dr_r[direction], c + dr_c[direction]

        return matrix 


tc1 = 3
tc2 = 4
tc3 = 10

print(Solution().generateSpiral(tc1))
print(Solution().generateSpiral(tc2))
print(Solution().generateSpiral(tc3))