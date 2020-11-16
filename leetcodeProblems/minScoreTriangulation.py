"""
    Problem statement:
        Given N, consider a convex N-sided polygon with vertices labelled A[0], A[i], ..., A[N-1] in clockwise order.

        Suppose you triangulate the polygon into N-2 triangles.  For each triangle, the value of that triangle is 
        the product of the labels of the vertices, and the total score of the triangulation is the sum of these values 
        over all N-2 triangles in the triangulation.

        Return the smallest possible total score that you can achieve with some triangulation of the polygon
"""
class Solution():
    def minScoreTriangulation(self, A):
        n = len(A)
        #construct a 2d matrix for returning the states
        dp = [[0 for i in range(len(A))] for _ in range(len(A))]

        #to form a traingle, we need atleast 3 sides
        #i, j, k where k should be k=i+2
        for k in range(2, len(A)):
            for i in range(n-k):
                start, end = i, i+k
                dp[start][end] = float("inf")
                #just find all combinations of j
                for j in range(start+1, end):
                    dp[start][end] = min(dp[start][end], dp[start][j] + dp[j][end] + A[start] * A[j] * A[end])
        
        return dp[0][-1]

tc1 = [1,2,3]
tc2 = [3,7,4,5]
tc3 = [1,3,1,4,1,5]

print(Solution().minScoreTriangulation(tc1))
print(Solution().minScoreTriangulation(tc2))
print(Solution().minScoreTriangulation(tc3))