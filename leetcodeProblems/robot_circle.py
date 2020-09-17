"""
  Problem Statement:
      On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:
      
      "G": go straight 1 unit;
      "L": turn 90 degrees to the left;
      "R": turn 90 degress to the right.
      The robot performs the instructions given in order, and repeats them forever.

      Return true if and only if there exists a circle in the plane such that the robot never leaves the circle
"""

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        #currently the robot is facing north
        direction_map = {'N':['W','E'],
                         'S':['E','W'],
                         'W':['S','N'],
                         'E':['N','S']}
        
        #coords map
        coords_map = {'N':[0, 1],'S':[0,-1],'W':[1,0],'E':[-1,0]}
        #currently facing
        facing = 'N'
        
        x, y = 0, 0
        
        for command in instructions:
            if command == 'L':
                facing = direction_map[facing][0]
            elif command == 'R':
                facing = direction_map[facing][1]
            else:
                x += coords_map[facing][0]
                y += coords_map[facing][1]
        
        if x == 0 and y == 0:
            return True
        
        return facing != 'N'
