import heapq
import re
import collections

class Solution:
    def mostCommonWord(self, paragraph, banned]):
        #remove special characters from the string
        paragraph = ' '.join(re.split(r"['.;!?,]", paragraph))
        paragraph = paragraph.replace("  "," ") #replace two space by one
        splitbyWords = paragraph.split(" ")
        print(splitbyWords)
        
        hashmap = collections.Counter(
            word for word in paragraph.lower().split())
        
        heap = []
        
        for word, freq in hashmap.items():
            if word in banned:
                pass
            else:
                heapq.heappush(heap, (-freq, word))
        
        mostFreq, word = heapq.heappop(heap)
        
        return word
