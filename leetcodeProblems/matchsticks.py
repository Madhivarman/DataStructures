"""
  Problem Statement:
      You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. 
      You want to use all the matchsticks to make one square. You should not break any stick, but you can link 
      them up, and each matchstick must be used exactly one time.

      Return true if you can make this square and false otherwise.
"""
class Solution:
    def makesquare(self, sticks: List[int]) -> bool:
        sticks = sorted(sticks, reverse=True)
        N, S = len(sticks), sum(sticks)
        if N < 4 or S % 4 or sticks[0] > S / 4:
            return False
        #max val, taken sides
        side, taken = S / 4, set()

        def dfs(i: int, target: int) -> bool:
            if i == N:
                return False
            if i in taken:
                return dfs(i + 1, target)
            cur = sticks[i]
            if cur <= target:
                taken.add(i)
                if cur == target or dfs(i + 1, target - cur):
                    return True
                taken.remove(i)
            return dfs(i + 1, target)

        for _ in range(3):
            if not dfs(0, side):
                return False
        return True
