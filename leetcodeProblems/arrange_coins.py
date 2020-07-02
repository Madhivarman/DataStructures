class Solution():
    def buildStairCase(self, steps, totalsteps):
        #print(steps, totalsteps)
        if steps >= totalsteps:
            return steps
        steps += 1
        diff = totalsteps - steps
        return self.buildStairCase(steps, diff)
    

    def optimalSolution(self, n):
        s = 1
        diff = n - 1
        
        while(True):
            #print(s, diff)
            if diff < 0:
                return s - 1
            if diff == 0:
                return s
            #print("*" * s)
            s += 1
            diff -= s
            


    def arrangeCoins(self, n):
        return self.buildStairCase(1, n-1)


tc1 = 5
tc2 = 8
tc3 = 10
tc4 = 20
tc5 = 100

print(Solution().optimalSolution(tc1))
print(Solution().optimalSolution(tc2))
print(Solution().optimalSolution(tc3))
print(Solution().optimalSolution(tc4))
print(Solution().optimalSolution(tc5))