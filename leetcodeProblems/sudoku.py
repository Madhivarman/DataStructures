import numpy as np
class Solution:
    def checkifValid(self, arr):
        valid = True
        seen = []#create a set
        for l in arr:
            if l not in seen or l == '.':
                seen.append(l)
            else:
                valid = False
                return valid
            
        return valid
                      
    def isValidSudoku(self, board):

        print(board)

        isvalid = True

        #resize the array into 3x3
        as_grid = []
        g1, g2, g3 = [], [], []
        col = [[] for _ in range(len(board))]

        def check_for_column(a):
            column_valid = True

            for num in range(len(a)):
                #append to the column to see
                if a[num] not in col[num] or a[num] == '.':
                    col[num].append(a[num])
                else:
                    print(col)
                    return False

            return column_valid

        for arr in board:
            #check if row is valid first
            if self.checkifValid(arr):
                pass
            else:
                return False

            grid_array = np.array(arr).reshape(3, 3)
            if grid_array.size == 9:
                g1.append(grid_array[0])
                g2.append(grid_array[1])
                g3.append(grid_array[2])
            
            #if the 3x3 is formed check if the grid is valid
            if len(g1) == 3 and len(g2) == 3 and len(g3) == 3:
                g1 = np.concatenate(g1)
                g2 = np.concatenate(g2)
                g3 = np.concatenate(g3)

                col_g1 = check_for_column(g1)
                col_g2 = check_for_column(g2)
                col_g3 = check_for_column(g3)

                print(col_g1, col_g2, col_g3)

                if col_g1 and col_g2 and col_g3:
                    pass
                else:
                    return False
                
                g1_check = self.checkifValid(g1)
                g2_check = self.checkifValid(g2)
                g3_check = self.checkifValid(g3)
                
                if g1_check and g2_check and g3_check:
                    pass
                else:
                    return False
                
                #empty the grids
                g1, g2, g3 = [], [], []
        
        return isvalid

sudoku = [[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],
["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],
[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".","."]] #false
tc_2 = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

print(Solution().isValidSudoku(tc_2))