"""
  Given an array of integers A, We need to sort the array performing a series of pancake flips.

  In one pancake flip we do the following steps:

  Choose an integer k where 0 <= k < A.length.
  Reverse the sub-array A[0...k].
  For example, if A = [3,2,1,4] and we performed a pancake flip choosing k = 2, we reverse the sub-array [3,2,1], 
  so A = [1,2,3,4] after the pancake flip at k = 2.

  Return an array of the k-values of the pancake flips that should be performed in order to sort A. Any valid answer that 
  sorts the array within 10 * A.length flips will be judged as correct.
"""

class Solution():
    def filps(self, A):
       result, N = [], len(A)
       
       #iterate
       for i in range(N, 0, -1):
          pointer = A.index(i)
          
          if pointer == i - 1:
            continue
           
          if pointer != 0:
            A[:pointer+1] = A[:pointer+1][::-1]
            result.append(pointer+1)
          
          A[:i] = A[:i][::-1]
          result.append(i)
      
      return result
