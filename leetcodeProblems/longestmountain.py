"""
    Problem Statement:
        Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:
            B.length >= 3
            There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
            (Note that B could be any subarray of A, including the entire array A.)

            Given an array A of integers, return the length of the longest mountain. 

            Return 0 if there is no mountain.
"""
import copy
class Solution():
    def longestMountain(self, A):
        result = 0
        #for each index i we need to find the ascending order
        #in left subarray, and descending order in right subarray
        N = len(A)
        left = [0] * N
        right = [0] * N 

        for i in range(1, N):
            if A[i] > A[i-1]:
                left[i] = left[i-1] + 1
        
        for i in reversed(range(N-1)):
            if A[i] > A[i+1]:
                right[i] = right[i+1] + 1
        
        for i in range(N):
            if left[i] > 0 and right[i] > 0:
                result = max(result, left[i] + right[i] + 1)
        
        return result

tc1 = [2,1,4,7,3,2,5]
tc2 = [2,2,2]
tc3 = [1,2,2,2]

print(Solution().longestMountain(tc1))
print(Solution().longestMountain(tc2))
print(Solution().longestMountain(tc3))