"""
    Problem Statement:
        Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, 
        and return them in any order.
        The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1. 
        graph[i] is a list of all nodes j for which the edge (i, j) exists.
"""

class Solution():

    def helperUtil(self, node, graph, visits, targetnode):
        #iterate till visits is empty
        while(visits):
            #source node, target node, connections
            sn, tn, conns = visits.pop()
            print(sn,tn, conns)

            #get the connections from the graph
            tn_conns = graph[tn]

            for conn in tn_conns:
                if conn == targetnode:
                    temp = []
                    temp = conns + [conn]
                    self.paths.append(temp)
                else:
                    temp = []
                    temp = conns + [conn]
                    visits.append((tn, conn, temp))
            
        print("result:{}".format(self.paths))

        return self.paths


    def findPossiblePath(self, network):
        self.paths = []
        nodes = len(network)

        #create a network graph
        graph = {}
        for i in range(nodes):
            graph[i] = network[i]
        
        visits = []

        source_connections = graph[0]

        for tc in source_connections:
            #if source node have direct connections to the
            #target node
            if tc == nodes - 1:
                self.paths.append([0, tc])
            #type - (source node, connections, possible path)
            visits.append((0, tc, [0, tc]))
        
        print(visits)

        #params - (curr_node, graph, queue, last_node)
        path = self.helperUtil(0, graph, visits, nodes-1)

        return path

tc1 = [[1,2],[3],[3],[]]
tc2 = [[1,2,3],[4],[3],[4],[]]

print(Solution().findPossiblePath(tc1))
print()
print(Solution().findPossiblePath(tc2))
