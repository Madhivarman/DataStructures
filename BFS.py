from collections import defaultdict


class Graph:
	#initial graph
	def __init__(self):
		self.graph =  defaultdict(list)

	#add edge
	def addEdge(self,source,nodes):
		self.graph[source].append(nodes)

	def BFS(self,s):
		#keep track of visited list
		visited = [False]*(len(self.graph)+1)
		queue = [] #keep track queue

		visited[s] = True #mark startingnode as visited
		queue.append(s)

		while queue:
			node = queue.pop(0) #pop the node from queue
			print(node, end=" ")

			for i in self.graph[node]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True


#create a graph
g = Graph()

g.addEdge(0,1)
g.addEdge(0,2)	
g.addEdge(1,3)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(3,5)
g.addEdge(4,6)
g.addEdge(5,6)

g.BFS(0)