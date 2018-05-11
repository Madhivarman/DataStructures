class Graph:

	def __init__(self,vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
		self.result = [[0 for column in range(vertices)] for row in range(vertices)]

	def print_the_shortest_path(self,result):

		print("The shortest path from source to the destination is")
		print("---------------------------------------------------")

		for i in result:
			for j in i:

				if j == 999:
					print("INF", end=" ")
				else:
					print(j, end=" ")

			print()

	def floyd_warshal(self):
		for i in range(self.V):
			for j in range(self.V):
				take_min_weight = [] #list to store all weights
				for k in range(self.V):
					take_min_weight.append(min(self.graph[i][j],self.graph[i][k]+self.graph[k][j]))

				self.result[i][j] = min(take_min_weight)

		self.print_the_shortest_path(self.result)



g = Graph(4)

g.graph = [
			[0,2,999,999],
			[999,0,3,999],
			[999,999,0,1],
			[5,4,999,0]
		]

g.floyd_warshal()