"""
    Problem Statement:
         Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.
            '?' Matches any single character.
            '*' Matches any sequence of characters (including the empty sequence).
            The matching should cover the entire input string (not partial).
"""
def wildcardMatch(string_, pattern):
        m,n=len(string_),len(pattern)
        memo=set()

        def dfs(i,j):
            print('Now Calling for the function df:({},{})'.format(i, j))
            if i==m:#s all over
                if j==n or all(pattern[t]=="*" for t in range(j,n)):#remain p are all * 
                    return True
                else:
                    return False
            elif j==n or (i,j) in memo:
                return False
            
            memo.add((i,j)) #add into set

            if string_[i]==pattern[j] or pattern[j]=="?":
                return dfs(i+1,j+1)
            elif pattern[j]=="*":
                return dfs(i,j+1) or dfs(i+1,j)
            else:
                return False
        
        return dfs(0,0)


isMatch = wildcardMatch("xaylmz","x?y*z")
print(isMatch)