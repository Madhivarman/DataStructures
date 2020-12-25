class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        #base condition
        if not matrix:
            return result
        
        #if the pointer is at 1st row, move right
        #if the pointer is at 1st column, move down
        #if the pointer is at last row, move right
        what_direction = 0 #even direction means up, otherwise down
        r, c = len(matrix), len(matrix[0])
        rp, cp = 0,0 #row pointer, column pointer
        total_iteration = r * c
        visited_node = 1
        
        while(visited_node < total_iteration+1):
            #condition to break
            if len(result) == total_iteration:
                break
                
            #print(rp, cp)
            loop = True
            #print("stuck in main loop")
            #loop to travel towards same direction
            while loop:
                result.append(matrix[rp][cp])
                if what_direction % 2 == 0:
                    #print("dir->up:{},{}".format(rp, cp))
                    nr, nc = rp - 1, cp + 1
                    if 0 <= nr < r and 0 <= nc < c:
                        visited_node += 1
                        rp, cp = nr, nc
                    else:
                        #change the direction
                        what_direction += 1
                        loop = False
                else:
                    #print("dir->down:{},{}".format(rp, cp))
                    #write logic to move downwards
                    nr, nc = rp+1, cp - 1
                    if 0 <= nr < r and 0 <= nc < c:
                        visited_node += 1
                        rp, cp = nr, nc
                    else:
                        what_direction += 1
                        loop = False
            
            #check for which direction the pointer should
            #move towards
            if (rp == 0 and cp != len(matrix[0]) - 1) or rp == len(matrix) - 1:
                cp += 1 #right
            else:
                rp += 1 #down
            
            loop = True
                
        
        return result
