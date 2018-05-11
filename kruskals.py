from collections import defaultdict

"""
	To find the MST using kruskal's Algorithm

	1. sort all edges in non-decresing order of their weight
	2. Pick the smallest edge. Check it forms the cycle with the constructed spanning trees so far
	3. Repeat until it formed (V-1) edge in the spanning tree
"""
class Graph:

	def __init__(self,vertices):

		self.V =  vertices
		self.graph = list()

	def addEdge(self,src,dest,weight):

		self.graph.append([src,dest,weight])


	def  find(self,parent,node):
		if parent[node] == node:
			return node

		return self.find(parent,parent[node])

	def union(self,parent,rank,src,dest):

		x_root = self.find(parent,src)
		y_root = self.find(parent,dest)

		if rank[x_root] < rank[y_root]:
			parent[x_root] = y_root

		elif rank[x_root] > rank[y_root]:
			parent[y_root] = x_root

		else:
			parent[y_root] = x_root
			rank[x_root] += 1

	def print_the_MST(self,result):

		print("The construction of MST is:")
		print("-----------------------------------------")

		for src,dest,weight  in result:
			print("{source}-{destination} ===> {weight}".format(source=src,destination=dest,weight=weight))

	def kruskals(self):
		result = [] #store result MST
		#sort the graph in non decreasing order
		self.graph = sorted(self.graph, key = lambda item:item[2])
		
		parent = []
		rank = []

		i = 0 #An index variable used for sorted edges
		e = 0 #An index variable used for calculating no.of.edges we have explored

		for node in range(self.V):
			#so far declare initial parent list and rank
			parent.append(node)
			rank.append(0)

		while e < self.V - 1:

			src,dest,wht = self.graph[i]
			i += 1 #increment the i for next exploring node
			x = self.find(parent,src)
			y = self.find(parent,dest)

			if x != y:
				e += 1 #increment the edge
				result.append([src,dest,wht])
				self.union(parent,rank,x,y)

		self.print_the_MST(result)



g = Graph(9)

g.addEdge(0,1,4)
g.addEdge(0,7,8)
g.addEdge(1,2,8)
g.addEdge(1,7,11)
g.addEdge(2,8,2)
g.addEdge(2,5,4)
g.addEdge(2,3,7)
g.addEdge(3,4,9)
g.addEdge(3,5,14)
g.addEdge(4,5,10)
g.addEdge(5,6,2)
g.addEdge(6,8,6)
g.addEdge(6,7,1)
g.addEdge(7,8,7)


g.kruskals()
