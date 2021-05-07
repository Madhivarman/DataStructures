"""
  Problem Statement:
    Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.
    In one step, you can delete exactly one character in either string.
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1_length = len(word1)
        word2_length = len(word2)
        
        #build a dp array
        dp = [[0 for _ in range(word2_length+1)] for _ in range(word1_length+1)]
        
        #step 1 -> longest subsequence
        for i in range(1, word1_length + 1):
            for j in range(1, word2_length + 1):
                #if ith and jth index character are same, increment
                #with previous number of matched characters
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        #formula to calculate delete operation required
        result = (word1_length + word2_length) - 2 * dp[-1][-1]
        return result
