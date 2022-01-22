class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        #base condition
        if root is None:
            return []
        
        result = []
        def dfs(node, level):
            if len(result) < level:
                result.append([])
            
            if node is not None:
                result[level-1].append(node.val)
                
            #iterate through the children
            for n in node.children:
                dfs(n, level+1)
        
        dfs(root, 1)
        return result
