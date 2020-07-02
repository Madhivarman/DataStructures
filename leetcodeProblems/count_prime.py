class Solution():
    def optimalMethod(self, n):
        totalPrimes = 0
        table = [True] * n
        
        for i in range(2, n):
            
            if table[i]:
                j, totalPrimes = 2, totalPrimes + 1
                #check for all multiplications till n
                while(j * i < n):
                    table[j * i] = False
                    j += 1 #increment the j
        
        return totalPrimes
        
    def bruteForece(self, n):
        initial_primes = [2, 3]
        #safe check
        if n == 0 or n == 1:
            return 0
        if n == 2 or n == 3:
            return n-2
        for i in range(4, n):
            #can divide with any of the prime number
            can_divide = False
            for j in initial_primes:
                if i % j == 0:
                    can_divide = True
                    break
            
            if can_divide:
                pass
            else:
                initial_primes.append(i)
        
        return len(initial_primes)
