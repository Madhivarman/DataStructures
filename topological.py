from collections import defaultdict

class Graph:

	def __init__(self,vertices):

		self.V = vertices
		self.graph = defaultdict(list)

	def addEdge(self,src,dest):

		self.graph[src].append(dest)


	def topologicalSortUtil(self,visited,node,stack):

		visited[node] = True

		for i  in self.graph[node]:

			if visited[i] == False:
				self.topologicalSortUtil(visited,i,stack)

		stack.insert(0,node)

	def print_the_topological_sort(self,stack):

		print("The Topological Order")
		print("-------------------------------------")

		stack_length = len(stack)

		for i in stack:
			print(i,end=" ")

	def topologicalSort(self):

		visited = [False]*self.V
		stack = [] #to store the stack result

		for i in range(self.V):
			if visited[i] == False:
				self.topologicalSortUtil(visited,i,stack)

		self.print_the_topological_sort(stack)



g = Graph(11)

g.addEdge(4,2)
g.addEdge(2,1)
g.addEdge(4,3)
g.addEdge(2,5)
g.addEdge(2,3)
g.addEdge(5,6)
g.addEdge(5,7)
g.addEdge(7,3)
g.addEdge(3,8)
g.addEdge(8,9)
g.addEdge(8,10)

g.topologicalSort()