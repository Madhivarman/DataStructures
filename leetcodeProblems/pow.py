class Solution():
    
    #exceeds time limit for larger numbers
    def power(self, x, n):
        temp = x
        for i in range(1, n):
            temp = temp*x
            #print(temp)
        return temp

    def pow(self, x, n):
        #optimal solution
        if n < 0:
            x = 1/x #value goes to denominator 
            n = abs(n) #power changes to positive
        
        res = 1
        while n != 0:
            if n % 2 != 0:
                res *= x
            
            x *= x
            n //= 2
        
        return res


print(Solution().pow(2.00000, 10), pow(2.00000, 10))
print("-" * 15)
print(Solution().pow(2.10000, 3), pow(2.10000, 3))
print("-" * 15)
print(Solution().pow(2.00000, -2), pow(2.00000, -2))
    
