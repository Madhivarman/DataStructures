"""
    Problem Statement:
        Given a 2D board and a list of words from the dictionary, find all words in the board.
        Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are
        those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

    Trie Data Structure Sample:
        {
            'p': {'e': {'a': {'*': True}}}, 
            'r': {'a': {'i': {'n': {'*': True}}}}, 
            'e': {'a': {'t': {'*': True}}}, 
            'o': {'a': {'t': {'h': {'*': True}, '*': True}}}
        }
"""

class Solution():

    def findWords(self, board, words):
        wordsmatched = set()
        #build the trie datastructure
        trie = self.build_trie(words)
        rows, cols = len(board), len(board[0])

        for row in range(rows):
            for col in range(cols):
                if board[row][col] in trie:
                    check_words = self.search(row, col, board, trie)
                    
                    #find all the words
                    for word in check_words:
                        wordsmatched.add(word)

        return wordsmatched
    
    def build_trie(self, words):
        trie = {}
        for word in words:
            curr = trie
            for char in word:
                curr = curr.setdefault(char, {})

            curr['*'] = True
        
        return trie
    
    def search(self, row, col, board, trie):
        matchedwords = []
        rows, cols = len(board), len(board[0])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] #up, down, left, right
        stack = [(row, col, trie, [], set())]

        while stack:
            curr_row, curr_col, curr_trie, matched_word, seen = stack.pop()
            #create a copy for overwrite
            curr_trie, matched_word, seen = curr_trie.copy(), matched_word.copy(), seen.copy()

            #get the current character
            char = board[curr_row][curr_col]

            if char not in curr_trie:
                continue
            matched_word.append(char)
            seen.add((curr_row, curr_col)) #mark the cell as seen

            if '*' in curr_trie[char]:
                matchedwords.append("".join(matched_word))
            
            #update the trie pointer
            curr_trie = curr_trie[char]

            for row_offset, col_offset in directions:
                #next row and next col
                next_row, next_col = row_offset + curr_row, col_offset + curr_col
                #condition check
                if 0 <= next_row < rows and 0 <= next_col < cols and (next_row, next_col) not in seen:
                    stack.append((next_row, next_col, curr_trie, matched_word, seen))
        
        return matchedwords

board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

words = ["oath","pea","eat","rain", "oat"]

print(Solution().findWords(board, words))