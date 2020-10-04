"""
  Problem Statement:
    Given a list of intervals, remove all intervals that are covered by another interval in the list.

    Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.

    After doing so, return the number of remaining intervals.
"""
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        total_intervals = 1
        
        hashmap = {}
        
        #sort the intervals
        intervals.sort()
        
        for s, e in intervals:
            if s not in hashmap:
                hashmap[s] = [[s,e]]
            else:
                hashmap[s].append([s,e])

        #sort by 1 key
        interim_lists = []
        
        for k, v in hashmap.items():
            temp = v
            temp.sort(key=lambda s: s[1], reverse=True)
            interim_lists.extend(temp)
        
        #print(interim_lists)
        
        start, end = interim_lists[0][0], interim_lists[0][1]
        
        for s, e in interim_lists[1:]:
            if (s >= start and s <= end) and (e <= end):
                pass
            else:
                total_intervals += 1
                start = max(start, s)
                end = max(end, e)
        
        return total_intervals
        
