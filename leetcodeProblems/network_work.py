"""
  Problem Statement:
    There are n computers numbered from 0 to n-1 connected by ethernet cables connections forming a network where connections[i] = [a, b] 
    represents a connection between computers a and b. Any computer can reach any other computer directly or indirectly through the network.
    
    Given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them 
    between any pair of disconnected computers to make them directly connected. Return the minimum number of times you need to do this in order to 
    make all the computers connected. If it's not possible, return -1. 
"""

class Solution:
    def helperUtil(self, network, node, n):
        #when all nodes are visited
        if len(self.visited) == n:
            return changes
        
        if node not in self.visited:
            self.visited.append(node) #mark as visited
            #if the nodes are not already visited
            conns = network[node]
            for subnode in conns:
                if subnode not in self.visited:
                    self.helperUtil(network, subnode, n)
        
        
    def makeConnected(self, n, connections):
        self.changes = 0
        self.visited = []
        
        #to find if it has enough connections
        if len(connections) <= n - 1:
            return - 1
        
        #create a hashmap for the connections
        network = {}
        
        #initial network
        for i in range(n):
            network[i] = []
        
        #make connections
        for conn in connections:
            s, d = conn[0], conn[1]
            network[s].append(d)
            network[d].append(s)
            
        start_node = list(network.keys())[0]
        
        #helper function dfs
        for x in range(n):
            if x not in self.visited:
                self.helperUtil(network, x, n)
                self.changes
        return self.changes-1

tc1, tc1_conns = 6, [[0,1],[0,2],[0,3],[1,2],[1,3]]
print(Solution().makeConnected(tc1, tc1_conns))
