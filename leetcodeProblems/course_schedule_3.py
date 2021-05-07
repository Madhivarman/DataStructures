"""
  Problem Statement:
    There are n different online courses numbered from 1 to n. You are given an array courses where courses[i] = [durationi, lastDayi] 
    indicate that the ith course should be taken continuously for durationi days and must be finished before or on lastDayi.

    You will start on the 1st day and you cannot take two or more courses simultaneously.

    Return the maximum number of courses that you can take.
"""
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        #sort the course by duration first
        courses.sort(key=lambda x:(x[1], x[0]))
        #priority queue(max) to keep the course lists
        time, pq = 0, []
        
        for duration, deadline in courses:
            #count the time
            time += duration
            #add to the minimum heap
            heapq.heappush(pq, -duration)
            #to check if the course cannot be completed
            #within the deadline, then we need to swap
            if time > deadline:
                #take out the longest duration course from heap
                #and check for the swap or just undo we insert
                time += heapq.heappop(pq)
        
        return len(pq)
