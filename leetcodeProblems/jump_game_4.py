class Solution:
    def minJumps(self, arr: List[int]) -> int:
        step = 0
        
        if len(arr) == 1:
            return step
        
        idx_map = defaultdict(list)
        
        #create a dictionary
        for idx, v in enumerate(arr):
            if v not in idx_map:
                idx_map[v] = [idx]
            else:
                idx_map[v].append(idx)
        
        #queue
        q = deque([0])
        
        while(q):
            step += 1
            size = len(q)
            
            for i in range(size):
                idx = q.popleft()
                # idx - 1
                if (idx - 1 >= 0 and idx_map[arr[idx-1]]):
                    q.append(idx-1)

                #idx + 1
                if (idx + 1 < len(arr) and idx_map[arr[idx+1]]):
                    if idx + 1 == len(arr) - 1:
                        return step 
                    q.append(idx+1)
                
                #containes in map
                if arr[idx] in idx_map:
                    for k in idx_map[arr[idx]]:
                        if k != idx:
                            if k == len(arr) - 1:
                                return step
                            q.append(k) 
                
                    del idx_map[arr[idx]]
                
        return step
