
class Graph:

	def __init__(self,vertices):
		self.v = vertices
		self.graph = [[0 for columns in range(vertices)] for rows in range(vertices)]


	def printsolution(self,distance):
		#iterate through each distance:
		print("Minimum distance from Source 0 to Destination \n")
		print("Destination \t Weight")
		print("------------\t -----------")
		for dist in range(self.v):
			print("{}\t\t{}".format(dist,distance[dist]))

	def minimumDistance(self,dist,sptset):
		#iterate through each vertex
		minimum = 1000 #default set minimum value
		for i in range(self.v):

			if dist[i] < minimum and sptset[i] == False:
				minimum = dist[i]
				min_index = i


		return min_index

	def dijisktras(self,src):
		dist = [1000]*self.v
		sptset = [False]* self.v

		dist[src] = 0 #mark it as zero

		for nodes in range(self.v):
			#find minimum distance
			u = self.minimumDistance(dist,sptset)
			sptset[u] = True #mark it as visited or True
			
			for v in range(self.v):
				if self.graph[u][v] > 0 and sptset[v] == False and dist[v] >  dist[u] + self.graph[u][v]:
					dist[v] = dist[u] + self.graph[u][v]
		

		self.printsolution(dist)




g = Graph(9)
g.graph = [
		   [0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
		]


g.dijisktras(3)