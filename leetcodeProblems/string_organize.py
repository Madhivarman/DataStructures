"""
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.
If possible, output any possible result.  If not possible, return the empty string.
"""

from collections import Counter
import heapq

class Solution():
    def organizeString(self, string):
        res = ''
        hashmap = Counter(string)
        heap = [] 

        #iterate through the dict
        for char, count in hashmap.items():
            #convert positive to negative, so when
            #using min heap map the more freq number 
            #will appear first
            heapq.heappush(heap, (-count, char))
        
        while(len(heap) > 1):
            print(heap)
            pl_count, pl = heapq.heappop(heap) #primary count, primary letter
            sl_count, sl = heapq.heappop(heap) #secondary count, secondary letter
            
            while(sl_count != 0):
                res += pl #concat
                res += sl #concat

                pl_count += 1 #update count
                sl_count += 1 #update count
            
            heapq.heappush(heap, (pl_count, pl)) #push the first letter again to the heap

        rc, rl = heapq.heappop(heap)

        if rc == 0:
            return res
        
        if rc == -1:
            res += rl
            return res
        else:
            res = ''

        return res
        

tc1 = 'aab'
tc2 = 'aaaab'
tc3 = 'aaabbccd'
tc4 = 'aabcdaabd'
tc5 = 'aaab'
tc6 = 'baaba'

template = '-' * 15

print("{}>{}".format(template, Solution().organizeString(tc1)))
print("{}>{}".format(template, Solution().organizeString(tc2)))
print("{}>{}".format(template, Solution().organizeString(tc3)))
print("{}>{}".format(template, Solution().organizeString(tc4)))
print("{}>{}".format(template, Solution().organizeString(tc5)))
print("{}>{}".format(template, Solution().organizeString(tc6)))