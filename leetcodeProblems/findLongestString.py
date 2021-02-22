"""
  Problem Statement:
    Given a string and a string dictionary, find the longest string in the dictionary that can 
    be formed by deleting some characters of the given string. If there are more than one possible 
    results, return the longest word with the smallest lexicographical order. If there is no 
    possible result, return the empty string.
"""
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d = sorted(d)
        d = sorted(d, key=len, reverse=True)
        
        for word in d:
            j = 0
            for i in range(len(s)):
                if s[i] == word[j]:
                    j += 1
                
                if j == len(word):
                    return word
        
        return ""
        
s = "abpcplea"
d = ["ale","apple","monkey","plea"]

print(Solution().findLongestWord(s, d))
