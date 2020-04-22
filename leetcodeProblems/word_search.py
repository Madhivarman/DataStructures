class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def search(i,j,word):
            if word == "":
                return True
            temp = board[i][j]
            board[i][j] = ""
            up, down, left, right = False, False, False, False

            if i > 0 and board[i-1][j] == word[0]:
                up = search(i-1, j, word[1:])

            if i < len(board)-1 and board[i+1][j] == word[0]:
                down = search(i+1, j, word[1:])

            if j > 0 and len(board) and board[i][j-1] == word[0]:
                left = search(i, j-1, word[1:])

            if j < len(board[0]) - 1 and board[i][j+1] == word[0]:
                right = search(i, j+1, word[1:])
                
            if up or down or left or right:
                return True
            board[i][j] = temp
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if search(i,j,word[1:]) == True: 
                        return True
        return False
