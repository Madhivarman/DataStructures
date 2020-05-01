"""
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

    Only one letter can be changed at a time
    Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

Note:

    Return an empty list if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.
    You may assume no duplicates in the word list.
    You may assume beginWord and endWord are non-empty and are not the same.
"""
from collections import deque

class Solution():
    def findLadders(self, start_word, end_word, wordlist):
        result = []
        words_visited = set(wordlist)

        q = deque()
        alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

        steps = 0
        minimum_steps = float('inf')

        q.append((start_word, [start_word])) #(curr_word, <list of words in Order>)

        while(q):
            size = len(q)
            remove = set() #list of words to remove from the dictionary
            steps += 1 #increment the steps

            if(steps > minimum_steps):
                break

            for _ in range(size):
                word, seq = q.popleft()
                #iterate through length of words
                for i in range(len(word)):
                    for j in alphabets:
                        formed_word = word[:i] + j + word[i+1:]
                        if(formed_word == end_word):
                            #append the seq into result
                            result.append(seq+[endword])
                            steps = 1
                            minimum_steps = 1
                        elif(formed_word in words_visited):
                            remove.add(formed_word)
                            q.append((formed_word, seq + [formed_word])) #append to the queue
            
            #remove the words from the words visited
            for rm in remove:
                words_visited.remove(rm)

        return result

startword = 'a'
endword = 'c'
wordlist = ['a','b','c']

print(Solution().findLadders(startword, endword, wordlist))