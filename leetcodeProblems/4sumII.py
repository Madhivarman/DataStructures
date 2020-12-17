"""
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the 
result is guaranteed to be at most 231 - 1.
"""

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        count = 0
        hashmap_ab, hashmap_cd = {}, {}
        
        def create_map(a, b):
            hashmap = {}
            for i in range(len(a)):
                for j in range(len(b)):
                    sum_ = a[i] + b[j]
                    if sum_ not in hashmap:
                        hashmap[sum_] = 1
                    else:
                        hashmap[sum_] += 1
            
            return hashmap
        
        hashmap_ab = create_map(A, B)
        hashmap_cd = create_map(C, D)
        
        count = sum(hashmap_ab[k] * hashmap_cd[-k] for k, v in hashmap_ab.items() if -k in hashmap_cd)
        
        return count
