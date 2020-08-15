"""
	Problem Statement:
		Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
"""

class Solution():
	def eraseOverLapIntervals(self, intervals):
		nonOverLapInterval = 0
		intervals = sorted(intervals)
		end = intervals[0][0] - 1
		
		for s, e in intervals:
			if end > s:
				end = min(end, e)
			else:
				nonOverLapInterval += 1
				end = e
		
		return len(intervals) - nonOverLapInterval

tc1 = [[1,2],[2,3],[3,4],[1,3]]
tc2 = [[1,2],[1,2],[1,2]]

print(Solution().eraseOverLapIntervals(tc1))
print(Solution().eraseOverLapIntervals(tc2))
