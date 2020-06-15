import random
import json

class Solution:
    def __init__(self, total):
        self.falseBuild = random.randint(0, total)
        self.m = total
        self.build = {}       
        self.isBadBuild()
        self.write()
        self.read()
    
    def read(self):
        with open('BuildConfig.json', 'r') as fp: 
            self.build = json.load(fp)
    
    def write(self):
        with open('BuildConfig.json', 'w') as fp:
            fp.write(json.dumps(self.build, indent=2))
    
    def isBadBuild(self):
        for i in range(self.m+1):
            if i < self.falseBuild:
                self.build[i] = False
            else:
                self.build[i] = True

    #we are traversing the build from the back so the time complexity
    #would be O(log n)
    #worst case would be O(n), if the first build itself an failure
    def OptimalSolution(self, n):
        if n == 1:
            return n

        if self.build[str(n)] and self.build[str(n-1)]:
            return self.notOptimalSolution(n-1)
        else:
            return n
    

    def firstBadVersion(self, n):
        l = 0
        r = n

        #using binary search tree
        #O(log n)
        while(l < r):
            mid = (l+r) // 2
            if not self.build[mid]:
                l = mid + 1
            else:
                r = mid
        
        return r



#print(Solution(100000).firstBadVersion(100000)) #0.24s
print(Solution(1000).OptimalSolution(1000)) #0.11s