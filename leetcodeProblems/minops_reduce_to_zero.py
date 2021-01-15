from itertools import accumulate

class Solution:
    def minOperations(self, nums, x) :
        cumsum = [0] + list(accumulate(nums))
        dic = {c:i for i,c in enumerate(cumsum)}
        print(dic)
        goal = cumsum[-1] - x
        ans = -float("inf")

        if goal < 0: return -1

        for num in dic:
            if num + goal in dic:
                ans = max(ans, dic[num + goal] - dic[num])
                print((num + goal), ans)

        return len(nums) - ans if ans != -float("inf") else -1

nums = [1,1,4,2,3]
x = 5

print(Solution().minOperations(nums, x))
