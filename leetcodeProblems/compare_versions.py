from collections import deque

class Solution:
    def compareVersion(self, version1, version2):
        v1 = deque(list(map(int, version1.split("."))))
        v2 = deque(list(map(int, version2.split("."))))

        while v1 or v2:
            val1 = v1.popleft() if v1 else 0 #if v1 is a valid
            val2 = v2.popleft() if v2 else 0 #if v2 is valid

            if val1 > val2:
                return 1
            elif val1 < val2:
                return -1
        
        return 0

tc1_v1, tc1_v2 = "7.5.2.4", "7.5.3"
tc2_v1, tc2_v2 = "1.001", "1.00001"

print(Solution().compareVersion(tc1_v1, tc1_v2))
print(Solution().compareVersion(tc2_v1, tc2_v2))
