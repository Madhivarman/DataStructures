"""
    Problem Statement:
        Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
        Note that the row index starts from 0.
"""

class Solution():
	def pascalTriangleIndex(self, k):
		if k == 0:
			return [1]
		if k == 1:
			return [1,1]

		output = [1, 1] #initial settings
		pointer = 1 #start from pointer

		while(pointer < k):
			o = [1] * (len(output) + 1)
			j = 0
			while(j < len(output)):
				o[j+1] = output[j+1] + output[j]
				j += 1

			output = o #update the output
			pointer += 1 #update the increment

		return output
