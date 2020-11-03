"""
    Problem Statement:
        Given an array of meeting intervals consisting of start and end time [[s1, e1],[s2, e2]]
        find the minimum number of conference room required  
"""
from heapq import heapify, heappush, heappop

class Solution():
    def minimumNumberOfConferenceRoom(self, intervals):
        rooms = []
        heapify(rooms)
        #sort by intervals by start time
        intervals.sort()
        heappush(rooms,intervals[0][1])

        for i in range(1, len(intervals)):
            earliest = heappop(rooms)
            current = intervals[i][0]
            end = intervals[i][1]

            if current >= earliest:
                heappush(rooms, end)
            else:
                heappush(rooms, earliest)
                heappush(rooms,end)
            
        return len(rooms)

intervals_tc1 = [[0,30], [5,10], [15, 20]]
intervals_tc2 = [[7,10], [2,4]]

print(Solution().minimumNumberOfConferenceRoom(intervals_tc1))
print(Solution().minimumNumberOfConferenceRoom(intervals_tc2))
