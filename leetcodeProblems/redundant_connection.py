"""
    Problem Statement:
        In this problem, a tree is an undirected graph that is connected and has no cycles.
        The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), 
        with one additional edge added. The added edge has two different vertices chosen from 1 to N, and was 
        not an edge that already existed.
        
        The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v, 
        that represents an undirected edge connecting nodes u and v.

        Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are 
        multiple answers, return the answer that occurs last in the given 2D-array. The answer edge [u, v] 
        should be in the same format, with u < v.
"""

class Solution():

    def findUnion(self, i):
        if self.sets[i] == -1:
            return i
        
        self.sets[i] = self.findUnion(self.sets[i])
        return self.sets[i]

    def makeUnion(self, u, v):
        iset = self.findUnion(u)
        jset = self.findUnion(v)

        if iset ==  jset:
            return False
        
        self.sets[iset] = jset
        return True

    def redundantConnection(self, connections):
        self.sets = [-1] * len(connections)
        red_connection = [] #redundant connection

        #using disjoin algorithm
        #1.create set
        #2. find set
        #3. union

        for u, v in connections:
            if self.makeUnion(u-1, v-1) == False:
                red_connection.append([u, v])
        
        return red_connection[-1]



tc1 = [[1,2], [1,3], [2,3]]
tc2 = [[1,2], [2,3], [3,4], [1,4], [1,5]]
tc3 = [[1,2], [2,1], [3,4], [1,4], [1,5]]
tc4 = [[1,4],[3,4],[1,3],[1,2],[4,5]]

print(Solution().redundantConnection(tc1))
print(Solution().redundantConnection(tc2))
print(Solution().redundantConnection(tc3))
print(Solution().redundantConnection(tc4))