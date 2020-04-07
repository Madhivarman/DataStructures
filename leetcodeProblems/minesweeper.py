"""
    Problem Statement:
        You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines, digit ('1' to '8') represents how many mines are adjacent to this revealed square, and finally 'X' represents a revealed mine.
        Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the board after revealing this position according to the following rules:

        If a mine ('M') is revealed, then the game is over - change it to 'X'.
        If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
        If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
        Return the board when no more squares will be revealed.
"""

class Solution():
    def __init__(self):
        self.direction = [(0,-1),(0,1),(1,0),(-1,0),(-1,-1),(1,1),(1,-1),(-1,1)]
    

    def checkAdjacentNodes(self, board, x, y):
        #still don't know how many mines are there
        count = 0
        #try all the possible route
        for dx, dy in self.direction:
            #next step x, y
            nx, ny = x + dx, y + dy

            #check if next move is valid
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == 'M':
                count += 1 #increment the counter
        
        return count
    
    def updateBoard(self, board, start_position):
        #starting position itself an mine, return the board
        x, y = start_position[0], start_position[1]
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        
        #reveal nearby adjacent mines
        nearbymines = self.checkAdjacentNodes(board, x, y)

        if nearbymines != 0:
            #update the number in the cell
            board[x][y] = str(nearbymines)
            return board
        else:
            #update the cell as B
            board[x][y] = 'B'
            #recursive call the search is complete for all cel
            for dx, dy in self.direction:
                nx, ny = x+dx, y+dy
                
                #is movement is valid
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == 'E':
                    position = [nx, ny] #update the position
                    self.updateBoard(board, position)

        return board



tc1 = [['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

click = [3, 0]

tc2 = [['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

click2 = [1, 2]

print(Solution().updateBoard(tc1, click))
print(Solution().updateBoard(tc2, click2))