"""
  Problem statement:
    There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. The bricks have 
    the same height but different width. You want to draw a vertical line from the top to the bottom and cross the least bricks.

    The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick in this row from left to right.

    If your line go through the edge of a brick, then the brick is not considered as crossed. You need to find out how to draw 
    the line to cross the least bricks and return the number of crossed bricks.

    You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.
"""
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        brick_map = {} #to store key value pairs
        untouched = 0 #return maximum untouched value
        
        for row in wall:
            end = 0
            for brick in row:
                end += brick
                if end not in brick_map:
                    brick_map[end] = 1
                else:
                    brick_map[end] += 1
        
        output = len(wall)
        for key in brick_map:
            if len(wall) - brick_map[key] < output and key != sum(wall[0]):
                output = len(wall) - brick_map[key]
        return output
