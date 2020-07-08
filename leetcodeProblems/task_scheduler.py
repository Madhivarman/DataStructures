from collections import Counter

class Solution:
    def leastInterval(self, tasks, n):
        if n == 0:
            return len(tasks)
        
        hashmap = Counter(tasks) #hashmap
        max_count = max(hashmap.values()) #max count
        
        slots = max_count + n * (max_count - 1) #to calculate slots
        
        count = 0
        
        for k, v in hashmap.items():
            #for each tie in max frequency of the items
            #we need to add the extra slots
            if hashmap[k] == max_count:
                count += 1
        
        slots += (count - 1)
        
        if slots < len(tasks):
            return len(tasks)
        else:
            return slots
 
tc1, tc1_n = ["A","A","A","B","B","B","C","C","C"], 2
tc2, tc2_n = ["A","A","A","B","B","B"], 0
tc3, tc3_n = ["A","A","A","A","A","A","B","C","D","E","F","G"], 2
tc4, tc4_n = ["A","A","A","A","A","A","B","C","D","E","F","F","F","F","G"], 2

print(Solution().leastInterval(tc1, tc1_n))
print(Solution().leastInterval(tc2, tc2_n))
print(Solution().leastInterval(tc3, tc3_n))
print(Solution().leastInterval(tc4, tc4_n))
