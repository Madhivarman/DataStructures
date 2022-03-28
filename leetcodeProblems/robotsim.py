class Solution:
    def __init__(self):
        #direction coords
        self.coords = {
            'N':(0,1),
            'S':(0,-1),
            'E':(1,0),
            'W':(-1,0)
        }
        
    def move(self, x, y, direction, command, danger):
        idx = 0
        nx, ny = direction[0], direction[1]
        while(idx < command):
            if(x+nx, y+ny) in danger:
                break
            x += nx
            y += ny
            idx += 1
        return x, y
        
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        #direction
        left = {'N':'W','E':'N','S':'E','W':'S'}
        right = {'N':'E','E':'S','S':'W','W':'N'}
        obst = {(i,j):True for i, j in obstacles}
        
        direction = 'N'
        ri, rj = 0, 0
        best = 0
        
        for command in commands:
            if command != -1 and command != -2:
                move_direction = self.coords[direction]
                ri, rj = self.move(ri, rj, move_direction, command, obst)
            
            if command == -1:
                direction = right[direction]
            if command == -2:
                direction = left[direction]
            
            best = max(best, ri**2 + rj**2)
            
        return best
