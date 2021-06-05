"""
    Problem Statement:
        You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: 
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: 
        for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

        The lock initially starts at '0000', a string representing the state of the 4 wheels.

        You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

        Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.
"""
from collections import deque
class Solution():
    def increment_slot(self, char):
        if char == '9':
            return '0'
        inc = int(char) + 1
        return str(inc)
    
    def decrement_slot(self, char):
        if char == '0':
            return '9'
        dec = int(char) - 1
        return str(dec)

    def openLock(self, deadends, target):
        steps = 0
        visited = {} #for constant lookup
        queue = deque([])
        startposition = "0000"
        queue.append(startposition)
        #bfs approach
        while(len(queue) > 0):
            q_size = len(queue)
            while(q_size > 0):
                current_position = queue.popleft()
                #if current position in the dead end then quit the loop
                if current_position in deadends:
                    continue
                #if current position is the target
                if current_position == target:
                    return steps
                
                lock_length = len(current_position)

                for idx in range(lock_length):
                    #possibilities
                    p1 = current_position[0:idx] + self.increment_slot(current_position[idx]) + current_position[idx+1:]
                    p2 = current_position[0:idx] + self.decrement_slot(current_position[idx]) + current_position[idx+1:]

                    #add to the queue
                    if (p1 not in visited) and (p1 not in deadends):
                        visited[p1] = 1
                        queue.append(p1)
                    
                    if (p2 not in visited) and (p2 not in deadends):
                        visited[p2] = 1
                        queue.append(p2)
                q_size -= 1 #decrement the visited possibilities
            steps += 1 #increment the steps
        #if there is no way to open the lock
        return -1

tc1_deadends =  ["0201","0101","0102","1212","2002"]
tc1_target = "0202"

print(Solution().openLock(tc1_deadends, tc1_target))