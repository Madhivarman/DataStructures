""" 
    Given an integer array with even length, where different numbers in this array 
    represent different kinds of candies. Each number means one candy of the corresponding 
    kind. You need to distribute these candies equally in number to brother and sister. Return the 
    maximum number of kinds of candies the sister could gain. 
"""
import operator
from collections import deque

class Solution():
    #not a optimal solution tho!
    def distributeCandies(self, candies):
        maximum = 0
        hashmap = {}
        brother, sister = [], []

        for candy in candies:
            if candy not in hashmap:
                hashmap[candy] = 1
            else:
                hashmap[candy] += 1

        equal_distribution = len(candies) / 2

        sorted_d = dict(sorted(hashmap.items(), key=operator.itemgetter(1)))
        print('Dictionary in ascending order by value:{}'.format(sorted_d))

        for k, v in sorted_d.items():
            #if equal distribution is acheived then break
            if len(sister) == equal_distribution:
                break

            if v == 1:
                sister.append(k)
            else:
                brother.append(k * (v-1))
                sister.append(k)
        
        return len(set(sister))
    
    def optimalSolutionUsingQueue(self, candies):
        q = deque()
        sister, brother = {}, {}
        equal_distribution = len(candies)/2

        q.append(candies[0])

        for c in candies[1:]:
            q.append(c)

            #condition to break
            if(len(sister) == equal_distribution):
                break

            while(q):
                current_choice = q.popleft()
                #if current flavour is not in sister bucket then append
                if(current_choice not in sister):
                    sister[current_choice] = 1
                else:
                    if current_choice in brother:
                        brother[current_choice] += 1
                    else:
                        brother[current_choice] = 1

        return len(set(sister))


candies = [1,1,2,3]
candies2 = [1,1,1,1,1,2,3,4,4,5]
candies3 = [1,1,2,2,3,3]

print(Solution().optimalSolutionUsingQueue(candies))
print(Solution().optimalSolutionUsingQueue(candies2))
print(Solution().optimalSolutionUsingQueue(candies3))