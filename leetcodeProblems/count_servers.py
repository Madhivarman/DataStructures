class Solution:    
    def countServers(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rs, cs = defaultdict(list), defaultdict(list)
        res = set()
        row, col = len(grid), len(grid[0])
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    rs[i].append((i,j))
                    cs[j].append((i,j))
        
        print(rs, cs)
        
        for k in rs:
            if len(rs[k]) <= 1:
                continue
            for (r,c) in rs[k]:
                res.add((r,c))
                
        for k in cs:
            if len(cs[k]) <= 1:
                continue
            for (r,c) in cs[k]:
                res.add((r,c))
        
        return len(res)
