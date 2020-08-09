"""
	Problem Statement:
		We have two integer sequences A and B of the same non-zero length.
		We are allowed to swap elements A[i] and B[i].  Note that both elements are in the same index position in their respective 
		sequences.

		At the end of some number of swaps, A and B are both strictly increasing.  
		(A sequence is strictly increasing if and only if A[0] < A[1] < A[2] < ... < A[A.length - 1].)

		Given A and B, return the minimum number of swaps to make both sequences strictly increasing.  
		It is guaranteed that the given input always makes it possible.
"""

class Solution():
	def minimumSwap(self, A, B):
		swap = [0] * len(A)
		noswap = [0] * len(A)
		
		#inital settings
		swap[0] = 1 #considered swap has made
		noswap[0] = 0 #no swap made
		
		i = 1
		while(i < len(A)):
			#declare with initial val
			swap[i] = noswap[i] = len(A)
			
			#side check
			if A[i-1] < A[i] and B[i-1] < B[i]:
				noswap[i] = noswap[i-1]
				swap[i] = swap[i-1] + 1
			
			#cross check
			if A[i-1] < B[i] and B[i-1] < A[i]:
				noswap[i] = min(noswap[i], swap[i-1])
				swap[i] = min(noswap[i-1]+1, swap[i])
				
			i += 1 #increment
		
		return min(swap[-1], noswap[-1])
