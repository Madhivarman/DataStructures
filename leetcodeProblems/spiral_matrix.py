class  Solution:

    def spiralOrder(self, matrix):
        result = []
        #row movement => right, down, left ,up
        dr_r = [0, 1, 0, -1]
        #column movement => down, left, up, right
        dr_c = [1, 0, -1, 0]
        row, col = len(matrix), len(matrix[0])

        ischecked = [[False] * col for _ in range(len(matrix))]

        #initial pointer
        r, c, direction = 0, 0, 0

        #iterate through M*N times
        for _ in range(row * col):
            result.append(matrix[r][c])
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

        return result 



matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

matrix2 = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]

print(Solution().spiralOrder(matrix2))