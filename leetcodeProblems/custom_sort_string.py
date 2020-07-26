"""
  S and T are strings composed of lowercase letters. In S, no letter occurs more than once.
  
  S was sorted in some custom order previously. We want to permute the characters of T so that they match the order that S was sorted. 
  More specifically, if x occurs before y in S, then x should occur before y in the returned string.

  Return any permutation of T (as a string) that satisfies this property.
"""

from collections import Counter

class Solution:
      def customSortString(self, S, T):
            t_map = Counter(T)
            result = []
            
            #appending char present in both strings
            for char in S:
                if char in t_map:
                    result.append(char * t_map[char])
            
            #appending char present in d but not in S
            for char in T:
                if char not in S:
                    result.append(char)
            
            #join the result
            return "".join(result)
