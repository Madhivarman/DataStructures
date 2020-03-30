class Solution():

    def group_anagram(self, wordlists):
        anagram_words = {}

        for words in wordlists:
            aftersort = ''.join(sorted(list(set(words))))
            if aftersort not in anagram_words.keys():
                anagram_words[aftersort] = []
                #anagram_words[aftersort].append(words)
            
            anagram_words[aftersort].append(words)

        return list(anagram_words.values())


words = ["eat", "tea", "tan", "ate", "nat", "bat"]
words2 = ["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]

print(Solution().group_anagram(words))
print(Solution().group_anagram(words2))
