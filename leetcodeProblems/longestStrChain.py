"""
  Problem Statement:
    Given a list of words, each word consists of English lowercase letters.

    Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1
    to make it equal to word2. For example, "abc" is a predecessor of "abac".

    A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where
    word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

    Return the longest possible length of a word chain with words chosen from the given list of words.
"""
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        #word length map
        words.sort(key=len)
        cache = {}
        ans = 1
        
        for word in words:
            cache[word] = 1
            for i in range(len(word)):
                already_exists = word[:i] + word[i+1:]
                if already_exists in cache:
                    cache[word] = max(cache[word], cache[already_exists]+1)
                    ans = max(ans, cache[word])
        
        return ans
