from itertools import permutations

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        #return empty value
        if n == 0:
            return
        
        empty = ""
        empty = ''.join([empty+"{}".format(x) for x in range(1, n+1)])
        p = permutations(empty)
        dict_ = {}
        for num, comb in enumerate(p):
            if num == k-1:
                comb = ''.join(comb)
                return comb  

print(Solution().getPermutation(3, 4))