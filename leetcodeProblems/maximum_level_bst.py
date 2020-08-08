class Solution: 
    def dfs(self, lst, rst, stack, level):
        if level > len(stack):
            stack.append([])
        
        if lst is not None:
            stack[level-1].append(lst.val)
            self.dfs(lst.left, lst.right, stack, level+1)
        
        if rst is not None:
            stack[level-1].append(rst.val)
            self.dfs(rst.left, rst.right, stack, level+1)
        
        return stack
        
    def maxLevelSum(self, root: TreeNode) -> int:
        #while iterating through each node
        #keep tracking of its level
        stack = [[root.val]]
        maximum = root.val
        result = None
        
        lst = root.left
        rst = root. right
        
        level_order = self.dfs(lst, rst, stack, 2)
        
        #get the index of the maximum sum 
        for i, lst in enumerate(level_order):
            if sum(lst) > maximum:
                result = i + 1
                maximum = sum(lst) #update the sum
        
        return result
