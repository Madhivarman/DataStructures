"""
	Problem Statement:
		Given a binary tree, return the vertical order traversal of its nodes values.
		For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).
		Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, we report the values of the nodes in order 
		from top to bottom (decreasing Y coordinates).
		If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.
		Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.
"""
from heapq import heappush, heappop

class Solution:
    def traverse(self, node, x, y):
        if not node:
            return
        
        self.maf[x].append((y, node.val))
        self.traverse(node.left, x-1, y+1)
        self.traverse(node.right, x+1, y+1)
		
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
            self.maf = defaultdict(list)        
            self.traverse(root, 0, 0)
            heap, ans = [], []

            for x, lst in self.maf.items():
                heappush(heap, (x, sorted(lst)))

            while heap:
                ans.append([v for _, v in heappop(heap)[1]])

            return ans
		
