"""
  Problem Statement:
    Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length 
    and answer[i] is the distance from index i to the closest occurrence of character c in s.

    The distance between two indices i and j is abs(i - j), where abs is the absolute value function.
"""
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        characters_map = {}
        result = [0] * len(s)
        
        for idx, char in enumerate(s):
            if char in characters_map:
                characters_map[char].append(idx)
            else:
                characters_map[char] = [idx]
        
        idx = 0
        
        while(idx < len(s)):
            if s[idx] == c:
                pass
            else:
                indexes = characters_map[c]
                vals = [abs(i - idx) for i in indexes]
                result[idx] = min(vals)
                
            idx += 1 #increment
        
        return result
