"""
    Problem Statement:
        Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.
        In a UNIX-style file system, a period . refers to the current directory. Furthermore, a double period .. moves the 
        directory up a level.
        Note that the returned canonical path must always begin with a slash /, and there must be only a single slash / 
        between two directory names. The last directory name (if it exists) must not end with a trailing /. Also, the 
        canonical path must be the shortest string representing the absolute path.
"""

class Solution():
    def canonical_path(self, path):
        output = []
        
        #split
        split_path = path.split("/")
        
        #iterate
        for val in split_path:
            if val == '':
                continue
            elif val == '.':
                continue
            elif val == '..':
                if len(output) > 0:
                    output.pop() #pop the last directory
            else:
                output.append(val)
        
        #join the list
        if len(output) > 0:
            output = '/' + '/'.join(output)
        elif len(output) == 0:
            output = '/'
        else:
            pass
    
        return output
        

print(Solution().canonical_path('/Users/whitewolf/wfh/../..//'))
print("*" * 15)
print(Solution().canonical_path('/../'))
print("*" * 15)
print(Solution().canonical_path('/a/b///c/d//./..///../'))
print("*" * 15)