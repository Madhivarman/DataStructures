class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		
class Solution:
	
	def dfs(self, root, node):
		if root is None:
			root = TreeNode(node)
			return root
		if root.val > node:
			root.left = self.dfs(root.left, node)
		else:
			root.right = self.dfs(root.right, node)
		return root
	
	def bstFromPreOrder(self, preorderLists:List[int])->Optional[TreeNode]:
		result = None
		for node in preorderLists:
			result = self.dfs(result,node)
		return result
