"""
  Problem Statement:
      Given an array of strings strs, return the length of the longest uncommon subsequence between them. If the longest uncommon subsequence does not exist, return -1.
      An uncommon subsequence between an array of strings is a string that is a subsequence of one string but not the others.
      A subsequence of a string s is a string that can be obtained after deleting any number of characters from s.
      For example, "abc" is a subsequence of "aebdc" because you can delete the underlined characters in "aebdc" to get "abc". Other subsequences
      of "aebdc" include "aebdc", "aeb", and "" (empty string).
"""

class Solution:
    def isSubstring(self, s1, s2):
        if s1 == s2:
            return True
        m, n = 0, 0
        
        while(m < len(s1) and n < len(s2)):
            if s1[m] == s2[n]:
                m += 1
            n += 1 #increment
        
        return m == len(s1)
        
    def findLUSlength(self, strs: List[str]) -> int:
        ans = -1
        for i in range(len(strs)):
            s1 = strs[i]
            currlen = len(s1)
            flag = False
            for j in range(len(strs)):
                s2 = strs[j]
                if i != j and self.isSubstring(s1, s2):
                    flag = True
                    break
            
            if not flag:
                ans = max(ans, currlen)
        return ans
