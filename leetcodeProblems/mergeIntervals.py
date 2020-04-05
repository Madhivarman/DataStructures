"""
    Problem Statement:
        Given a collection of intervals, merge all overlapping intervals.
"""

class Solution():

    def mergeOverlapIntervals(self, interval_lists):
        overlap_range = []
        #sort the lists
        interval_lists = sorted(interval_lists)

        #if the list is empty
        if not interval_lists:
            return overlap_range
        
        for interval in interval_lists:
            if not overlap_range or overlap_range[-1][1] < interval[0]:
                #if overlap_range interval is simply empty
                #just append, if [1, 3] is in overlap range
                #and interval now is [4,6] just append to the
                #overlap_range
                overlap_range.append(interval)
            else:
                #update the last range 
                #if overlap_range[-1][1] = [4,6] and 
                #current interval is [5, 7], then overlap range
                #should change to [4, 7]
                overlap_range[-1][1] = max(overlap_range[-1][1], interval[1])

        return overlap_range

tc1 = [[1,3],[2,6],[8,10],[15,18]]
tc2 = [[1,4],[4,5]]
tc3 = [[20, 30],[1,22],[2,6],[5,10],[9,18]]
tc4 = []
tc5 = [[1,100],[2,5],[3,6],[6,10]]
tc6 = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]

print(Solution().mergeOverlapIntervals(tc1))
print(Solution().mergeOverlapIntervals(tc2))
print(Solution().mergeOverlapIntervals(tc3))
print(Solution().mergeOverlapIntervals(tc4))
print(Solution().mergeOverlapIntervals(tc5))
print(Solution().mergeOverlapIntervals(tc6))