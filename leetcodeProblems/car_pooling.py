"""
    Problem Statement:
        You are driving a vehicle that has capacity empty seats initially available for passengers.  
        The vehicle only drives east (ie. it cannot turn around and drive west.)

        Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information 
        about the i-th trip: the number of passengers that must be picked up, and the locations to pick them 
        up and drop them off.  The locations are given as the number of kilometers due east from your vehicle's 
        initial location.

        Return true if and only if it is possible to pick up and drop off all passengers for all the given trips.
"""

class Solution():
    def carPooling(self, trips, capacity):
        end_max = 0
        
        for p, s, e in trips:
            end_max = max(end_max, e)
        
        dp = [0] * (end_max + 2)
        
        for p, s, e in trips:
            dp[s] += p
            dp[e] -= p
        
        for stop in dp:
            capacity -= stop
            
            if capacity < 0:
                return False
        
        return True


tc1_trips, tc1_capacity = [[2,1,5],[3,3,7]], 4 #False
tc2_trips, tc2_capacity = [[2,1,5],[3,3,7]], 5 #True
tc3_trips, tc3_capacity = [[2,1,5],[3,5,7]], 3 #True
tc4_trips, tc4_capacity = [[3,2,7],[3,7,9],[8,3,9]],11
tc5_trips, tc5_capacity = [[7,5,6],[6,7,8],[10,1,6]], 16

print(Solution().carPooling(tc1_trips, tc1_capacity))
print(Solution().carPooling(tc2_trips, tc2_capacity))
print(Solution().carPooling(tc3_trips, tc3_capacity))
print(Solution().carPooling(tc4_trips, tc4_capacity))
print(Solution().carPooling(tc5_trips, tc5_capacity))