
from collections import defaultdict

class Graph:

	def __init__(self,vertices):

		self.V = vertices
		self.graph = defaultdict(list)

	def addEdge(self,src,dest):

		self.graph[src].append(dest)

	def find_parent(self,parent,node):

		if parent[node] == -1:
			return node

		if parent[node] != -1:
			return self.find_parent(parent,parent[node])


	def union(self,parent,x,y):
		x_set = self.find_parent(parent,x)
		y_set = self.find_parent(parent,y)

		parent[x_set] = y_set

	def detectCycle(self):
		parent = [-1]*self.V

		for i in range(self.V):

			for j in self.graph[i]:
				x = self.find_parent(parent,i)
				y = self.find_parent(parent,j)

				if x == y:
					return True

				self.union(parent,x,y)

g = Graph(9)

g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(4,5)
g.addEdge(5,6)
g.addEdge(6,7)
g.addEdge(7,8)
g.addEdge(8,6)

if g.detectCycle():
	print("Graph Contain Cycle")
else:
	print("Graph Does not Contain Cycle")