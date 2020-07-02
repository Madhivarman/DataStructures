"""
    Problem Statement:
        Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) 
        which sum to n.
"""

class Solution():
    def findPerfectSquare(self, n):
        #using dynamic programing method
        dp = [i for i in range(n+1)]

        pointer = 4 #start from the pointer 4

        while(pointer <= n):
            i = 1
            while(True):
                p = i * i
                temp = pointer - p
                #boundary check
                if temp < 0:
                    break

                dp[pointer] = min(dp[pointer], 1 + dp[temp])
                i += 1 #increment the i

            pointer += 1 #increment the pointer
            
        return dp[-1]
                


tc1 = 12
tc2 = 20
tc3 = 13
tc4 = 75
tc5 = 128

print(Solution().findPerfectSquare(tc1))
print(Solution().findPerfectSquare(tc2))
print(Solution().findPerfectSquare(tc3))
print(Solution().findPerfectSquare(tc4))
print(Solution().findPerfectSquare(tc5))