"""
Problem Statement:
  In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. 
  The order of the alphabet is some permutation of lowercase letters.

  Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only 
  if the given words are sorted lexicographicaly in this alien language.
"""


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapping = {c:i for i, c in enumerate(order)}
        words_agg = []
        
        for word in words:
            words_agg.append(tuple([mapping[c] for c in word]))
        
        print(words_agg)
        
        return words_agg == sorted(words_agg)
