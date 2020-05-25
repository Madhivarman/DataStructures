"""
    There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network 
    where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other 
    server directly or indirectly through the network.
    A critical connection is a connection that, if removed, will make some server unable to reach some other server.
    
    Return all critical connections in the network in any order.
"""

class Solution():
    def criticalConnection(self, network, n):
        self.criticalnetwork = []
        self.ap = [] #articulation point
        self.graph = {i:[] for i in range(n)}

        #iterate through the network
        for u, v in network:
            self.graph[u].append(v)
            self.graph[v].append(u)
        
        #initialization
        self.visitedTime = [0 for _ in range(n)]
        self.lowTime = [0 for _ in range(n)]
        self.visitedNode = [False for _ in range(n)]

        #dfs
        #root node =0, parent = -1, count = 0
        self.dfs(0, -1, 0)
        print("Articulation Point:{}".format(self.ap))
        return self.criticalnetwork
    
    def dfs(self, node, parent, count):
        
        if self.visitedNode[node]:
            return

        #mark it as visited
        self.visitedNode[node] = True
        self.visitedTime[node] = count
        self.lowTime[node] = count
        count += 1 #increment the count

        #traverse through the adjaceny nodes
        for neighbor in self.graph[node]:
            if neighbor == parent:
                continue

            if self.visitedNode[neighbor]:
                self.lowTime[node] = min(self.lowTime[node], self.lowTime[neighbor])
            else:
                #call back
                self.dfs(neighbor, node, count+1)
                self.lowTime[node] = min(self.lowTime[node], self.lowTime[neighbor])
                #check condition
                if self.visitedTime[node] < self.lowTime[neighbor]:
                    self.ap.append(node)
                    self.criticalnetwork.append([node, neighbor])


tc1_network, tc1_n = [[0,1],[1,2],[2,0],[1,3]], 4
print(Solution().criticalConnection(tc1_network, tc1_n))
