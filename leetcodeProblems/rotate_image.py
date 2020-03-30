import copy

class Solution:

    #rotate the give matrix 90 degree
    #with returning new matrix
    def rotate(self, matrix):
        row, column = len(matrix), len(matrix[0])-1

        new_matrix = copy.deepcopy(matrix)
        
        #iterate through the row
        rowindex = 0
        for rowpointer in range(row):
            #iterate through column
            colindex = 0
            for colpointer in range(column+1):
                #index to rotate
                colchange = column - rowindex
                #print('Index Changed from {} -> {}'.format((rowindex, colindex),(colindex, colchange)))
                new_matrix[colindex][colchange] = matrix[rowindex][colindex] 
                colindex += 1
            
            rowindex += 1

        return new_matrix
    
    #rotate to 90 degree with modifying
    #existing array
    def rotate_without_modifying(self, matrix):
        length = len(matrix)
        temp = [] #to store temporary solution
        for i in range(length):
            temp1 = []
            for j in range(length-1, -1, -1):
                temp1.append(matrix[j][i])
            
            temp.append(temp1)
        
        matrix.clear()
        matrix.extend(temp)

        return matrix


matrix = [  
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrix2 = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]

print(Solution().rotate_without_modifying(matrix2))
