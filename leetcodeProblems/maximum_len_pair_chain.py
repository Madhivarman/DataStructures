"""
  Problem Statement:
      You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.
      Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed 
      in this fashion.
      
      Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. 
      You can select pairs in any order.
"""

class Solution():
    def maximumLenPairChain(self, pairs):
        result = 0
        
        #safe check
        if len(pairs) == 0:
            return result
        
        #sort
        pairs.sort(key=lambda x: x[1])
            
        curr = float('-inf')
           
       for pair in pairs:
            x, y = pair
            #condition
            if curr < x:
                result += 1
                curr = y
       
       return result

tc1 = [[1,2], [2,3], [3,4]]
tc2 = [[-10,-8],[8,9],[-5,0],[6,10],[-6,-4],[1,7],[9,10],[-4,7]]

print(Solution().maximumLenPairChain(tc1))
print(Solution().maximumLenPairChain(tc2))
