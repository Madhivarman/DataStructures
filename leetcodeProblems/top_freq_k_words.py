"""
  Given a non-empty list of words, return the k most frequent elements.
  Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, 
  then the word with the lower alphabetical order comes first.
"""

class Solution:
    def topKFrequent(self, words, k):
        hashmap = {}
        
        #O(n)
        for word in words:
            if word in hashmap: 
                hashmap[word] += 1
            else: 
                hashmap[word] = 1
                
        #reverse the count to negative which bigger number
        #becomes smaller
        sort = sorted([ (-hashmap[word], word) for word in hashmap ])
        res = []
        
        #O(log n)
        for freq, val in sort[:k]: 
            res.append(val)
        
        return res

words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4

print(Solution().topKFrequent(words, k))
