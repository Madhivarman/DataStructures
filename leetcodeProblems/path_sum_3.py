"""
	Problem Statement:
		You are given a binary tree in which each node contains an integer value.
		Find the number of paths that sum to a given value.
		The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
		The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
"""
from collections import defaultdict

class Solution():
	
	def dfs(self, root, prefixes, currsum, target):
		if root is None:
			return
		
		currsum += root.val #add up curr val
		
		if currsum == target:
			self.count += 1
			
		if(currsum - target) in prefixes:
			self.count += prefixes[currsum - target]
		
		prefixes[currsum] += 1
		
		self.dfs(root.left, prefixes, currsum, target)
		self.dfs(root.right, prefixes, currsum, target)
		
		prefixes[currsum] -= 1
		
	def findPathSum(self, root, target):
		self.count = 0 
		prefixes = defaultdict(int) #using cumulative approach
		#params - (root, prefixes, currsum, target)
		currsum = 0
		self.dfs(root, prefixes, currsum, target)
		
		return self.count
