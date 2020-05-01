"""
    Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

    Only one letter can be changed at a time.
    Each transformed word must exist in the word list.

    Note:

    Return 0 if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.
    You may assume no duplicates in the word list.
    You may assume beginWord and endWord are non-empty and are not the same.
"""

from collections import deque

class Solution():
    def wordLadder(self, startword, endword, wordlist):
        edits = 1
        words_visited = {} #to store the wordlist
        q = deque()
        alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

        #condition
        if(endword not in wordlist):
            return 0
        
        #append the words to dictionary
        for word in wordlist:
            words_visited[word] = 1
        
        q.append(startword) #append start word to the queue

        #while q is not empty
        while(q):
            print("Queue:{}".format(q))
            wordlength = len(q)
            while(wordlength):
                x = q.popleft() #pop the leftmost word
                print("popping:{}".format(x))
                #iterate through the wordlength
                for i in range(len(startword)):
                    for j in alphabets:
                        formed_word = x[:i] + j + x[i+1:] #formed words
                        #if the end word is found
                        if(formed_word == endword):
                            edits += 1
                            return edits
                        
                        try:
                            del words_visited[formed_word]
                            q.append(formed_word) #append the word to the queue
                        except:
                            continue

                wordlength -= 1 #decrease the queue iteration
            edits+=1 #increse the edits                  

        return 0


startword = 'hit'
endword = 'cog'
wordlist = ['hot','dot','dog','lot','log','cog']

print(Solution().wordLadder(startword, endword, wordlist))