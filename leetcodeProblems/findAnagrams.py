"""
  Problem Statement:
      Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

      Strings consists of lowercase English letters only and the length of both strings s and p will 
      not be larger than 20,100.

      The order of output does not matter.
"""

from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        hashmap = Counter(p)
        stack = [] #to keep track

        for num, char in enumerate(s):
            if char in hashmap:
                if hashmap[char] > 0:
                    hashmap[char] -= 1 #decrement the count
                    stack.append(char) #append the character
                    #if it reaches the length of the p
                    if len(stack) == len(p):
                        result.append(num - len(p) + 1)
                        hashmap[stack.pop(0)] += 1

                else:
                    j = stack.index(char)
                    for y in stack[0:j]:
                        hashmap[y] += 1                    
                    stack = stack[j+1:] + [char]

            else:
                hashmap = Counter(p)
                stack.clear() #clear the stack
                
        return result
