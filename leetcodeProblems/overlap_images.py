"""
  Problem Statement:
      Two images A and B are given, represented as binary, square matrices of the same size.  (A binary matrix has only 0s and 1s as values.)

      We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of 
      the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.

      (Note also that a translation does not include any kind of rotation.)

      What is the largest possible overlap?
"""

class Solution:
    def largestOverlap(self, A, B) -> int:
        #using vectorizing method
        A_ones, B_ones, = [], []
        collections = {}
        
        #since it is square matrix, just 
        #iterating
        for row in range(len(A)):
            for col in range(len(A[0])):
                if A[row][col] == 1:
                    A_ones.append((row, col))
                
                if B[row][col] == 1:
                    B_ones.append((row, col))
        
        
        for r_a, c_a in A_ones:
            for r_b, c_b in B_ones:
                #vectorization formulae
                r, c = (r_b - r_a), (c_b - c_a)
                
                if (r, c) in collections:
                    collections[(r, c)] += 1
                else:
                    collections[(r, c)] = 1
        
        return max(collections.values() or [0])
