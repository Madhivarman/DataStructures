"""
    Problem Statement:
        Given an array A of integers, return true if and only if we can partition the array into three non-empty 
        parts with equal sums.

        Formally, we can partition the array if we can find indexes i+1 < j 
        with (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])
"""
class Solution():
    def canPartitionIntoThree(self, A):
        total = sum(A) // 3
        i = 0 
        pointer = 0
        bucket = [0] * 3
        
        #iterate through the list
        while(i < len(A)):
            #print(pointer, bucket, i)
            
            if pointer < 3:
                if bucket[pointer] < total or i != len(A) - 1:
                    bucket[pointer] += A[i]
            
                if bucket[pointer] == total:
                    pointer += 1 #increment the pointer
            
            if pointer < 3 and bucket[pointer] > total and i == len(A)-1:
                return False
            
            i += 1 #increment the pointer
        
        return True

tc1 = [0,2,1,-6,6,-7,9,1,2,0,1]
print(Solution().canPartitionIntoThree(tc1))