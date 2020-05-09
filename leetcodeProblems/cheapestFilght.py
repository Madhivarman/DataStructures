"""
    There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.
    Now given all the cities and flights, together with starting city src and the destination dst, your task is to 
    find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.
"""

from queue import PriorityQueue

class Solution():
    def findCheapestFilght(self, src, dest, routes, k, nodes):
        adj = {i: {} for i in range(n)}
        
        for u, v, w in routes:
            adj[u][v] = w
        
        dist = [float("inf") for i in range(n)]
        visited = [False for i in range(n)]
        dist[src] = 0

        print(adj)
        
        pq = PriorityQueue()
        pq.put((0, src, -1))
        visited[src] = True
        
        while not pq.empty():
            minDist, vertex, stops = pq.get()
            print(minDist, vertex, stops)
            if stops > k: continue
                
            if vertex == dest:
                return minDist
            
            for child in adj[vertex]:
                print(vertex, child)
                minChildDist = minDist + adj[vertex][child]
                if not visited[child]:
                    visited[vertex] = True
                    dist[child] = minChildDist
                    pq.put((minChildDist, child, stops + 1))

        return -1


routes = [[0,1,100],[1,2,120],[0,2,150]]
src, dest = 0, 2
k = 1
n = 3

print(Solution().findCheapestFilght(src, dest, routes, k, n))