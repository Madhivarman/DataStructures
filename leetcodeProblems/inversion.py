class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        max_prior = A[0]
        for i in range(2, len(A)):
            if A[i] < max_prior:
                return False
            max_prior = max(max_prior, A[i-1])
        
        return True
