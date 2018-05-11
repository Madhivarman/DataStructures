from collections import defaultdict

class Graph:

	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self,src,dest):
		self.graph[src].append(dest)

	def DFSUtil(self,s,visited):
		visited[s] = True #change the node as visited
		print(s, end = " ")

		for i in self.graph[s]:
			if visited[i] == False:
				self.DFSUtil(i,visited)

	def DFS(self,s):
		visited = [False]*(len(self.graph)+1)
		#DFS traversal
		self.DFSUtil(s,visited)

g = Graph()

g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(3,5)
g.addEdge(4,6)
g.addEdge(5,6)

g.DFS(0)