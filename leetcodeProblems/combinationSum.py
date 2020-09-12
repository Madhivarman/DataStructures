"""
    Problem Statement:
        Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 
        can be used and each combination should be a unique set of numbers.

        Note:
        All numbers will be positive integers.
        The solution set must not contain duplicate combinations.
"""
class Solution():
    def possibleCombinations(self, k, n):
        result = {}
        seen = set()

        #iterate through 1-9 to find the possible combination sum
        #of N
        for i in range(1, 10):
            temp = []
            temp.append(i) #initialize the current i

            for j in range(i+1, 10):

                #condition result
                if len(temp) == k and sum(temp) == n:
                    if tuple(temp) in result:
                        result[tuple(temp)] += 1
                    else:
                        result[tuple(temp)] = 1
                    
                    #initialize the temp for other combinations
                    temp[1:] = []
                
                elif len(temp) == k - 1:
                    diff = n - sum(temp)
                    #if only difference not in temp
                    if diff not in temp and diff > 0:
                        temp.append(diff)
                
                else:
                    temp.append(j)
        #returns all possible combinations
        return result.keys()
    
    def combinations(self, k, n):
        self.response = []
        self.dfs(k, n, [])
        return self.response
    
    def dfs(self, k, n, currsol):
        if k < 0 or n < 0:
            return
        
        if k == 0 and n == 0:
            self.response.append(currsol)
        
        start = currsol[-1] + 1 if currsol else 1

        for i in range(start, 10):
            self.dfs(k-1, n-i, currsol + [i])


tc1_k, tc1_n = 3, 7 #[[1,2,4]]
tc2_k, tc2_n = 3, 9 #[[1,2,6],[1,3,5],[2,3,4]]

print(Solution().combinations(tc1_k, tc1_n))
print(Solution().combinations(tc2_k, tc2_n))