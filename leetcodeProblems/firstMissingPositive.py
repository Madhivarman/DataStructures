def firstMissingPositive(self, nums):
        smallest = 1
        biggest = 0
        for i in nums:
            if i < 0:
                continue
            smallest = min(smallest, i)
            biggest = max(biggest, i)
        
        if smallest > 1:
            return 1
        for j in range(smallest, biggest):
            if j not in nums:
                return j
            
        return biggest + 1

result = firstMissingPositive([1,2,0])
print(result)