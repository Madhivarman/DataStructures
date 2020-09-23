"""
  Problem Statement:
    There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

    You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You 
    begin the journey with an empty tank at one of the gas stations.

    Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

    Note:

    If there exists a solution, it is guaranteed to be unique.
    Both input arrays are non-empty and have the same length.
    Each element in the input arrays is a non-negative integer.
"""
class Solution:
    def canCompleteCircuit(self, gas, cost):
        gas_tank, start_station = 0, 0
        
        if sum(gas) < sum(cost):
            return -1
        
        for i in range(len(gas)):
            gas_tank += gas[i] - cost[i]
            
            if gas_tank < 0:
                start_station = i + 1
                gas_tank = 0
        
        return start_station
