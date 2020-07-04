"""
    Problem Statement:
        Write a program to find the n-th ugly number.
        Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
"""

class Solution():
    def optimalSolution(self, n):
        result= [1] + [0] * (n-1)
        i2 = i3 = i5 = 0

        for i in range(1, n):
            result[i] = min(result[i2] * 2, result[i3] * 3, result[i5] * 5)
            if result[i] == result[i2] * 2:
                i2 += 1
            if result[i] == result[i3] * 3:
                i3 += 1 
            if result[i] == result[i5] * 5:
                i5 += 1
        
        return result[-1]

    def bruteForceApproach(self, n):
        result = []
        i = 2
        count = 1

        #helper fn
        def isUgly(m):
            isUgly = False
            while(True):
                cannotDivisible=True
                for p in [2,3,5]:
                    #can divisible
                    if m % p == 0:
                        cannotDivisible=False #change the flag
                        m /= p
                    
                if m == 1:
                    isUgly = True
                    return isUgly
                
                if cannotDivisible:
                    return 
            
            return isUgly
        
        while(count < n):
            if(isUgly(i)):
                result.append(i)
                count += 1
            
            i += 1 
        
        s = [1] + sorted(result)
        return s[n-1]


test_cases = [8, 10, 15, 100, 150, 200, 600, 1690]

for tc in test_cases:
    print(Solution().optimalSolution(tc))