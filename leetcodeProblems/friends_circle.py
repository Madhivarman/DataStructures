"""
    Problem Statement:
        There are N students in a class. Some of them are friends, while some are not. Their 
        friendship is transitive in nature. For example, if A is a direct friend of B, and B is a
        direct friend of C, then A is an indirect friend of C. And we defined a friend circle 
        is a group of students who are direct or indirect friends.


        Given a N*N matrix M representing the friend relationship between students in the class.
        If M[i][j] = 1, then the ith and jth students are direct friends with each other, 
        otherwise not. And you have to output the total number of friend circles among all the 
        students.
"""

class Solution():

    def dfs(self, mapping, node):
        self.visited[node] = True
        #print(node, self.visited, self.ngroups)
        #check if the node doesn't have any friends
        #look up other friends
        if len(mapping[node]) == 0 and node < len(self.visited)-1:
            self.visited[node] = True
            self.dfs(mapping, node+1)
        
        for friend in mapping[node]:
            if self.visited[friend] == False:
                self.ngroups -= 1 #decrement the group
                self.dfs(mapping, friend)
        
        return self.ngroups


    def groups(self, friends_matrix):
        self.ngroups = len(friends_matrix)
        student_friends = {}
        self.visited = [False for i in range(self.ngroups)]

        #consider each student as a node
        for i in range(len(friends_matrix)):
            student_friends[i] = []
        
        #iterate through matrix and set the graph straight
        for r in range(len(friends_matrix)):
            for c in range(len(friends_matrix[0])):
                if friends_matrix[r][c] == 1 and r != c:
                    student_friends[r].append(c)
        
        print('Student Graph:{}'.format(student_friends))

        start_from = 0

        #params - (friends map, visited, node, parent)

        for i in range(len(self.visited)):
            if self.visited[i] == False:
                self.ngroups = self.dfs(student_friends, i)

        return self.ngroups


tc1_fc = [[1,1,0],[1,1,0],[0,0,1]]
tc2_fc = [[1,1,0],[1,1,1],[0,1,1]]
tc3_fc = [[1,0,0],[0,1,0],[0,0,1]]
tc4_fc = [[1,0,1,1,0],[0,1,0,0,1],[1,0,1,1,0],[1,0,1,1,0],[0,1,0,0,1]]
tc5_fc = [[1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],[0,1,0,1,0,0,0,0,0,0,0,0,0,1,0],
    [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,1,0,0,0,1,0,0,0,1,0,0,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],[0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]]

print(Solution().groups(tc1_fc))
print(Solution().groups(tc2_fc))
print(Solution().groups(tc3_fc))
print(Solution().groups(tc4_fc))
print(Solution().groups(tc5_fc))