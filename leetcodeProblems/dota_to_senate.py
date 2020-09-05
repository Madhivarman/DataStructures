"""
  Problem Statement:
    In the world of Dota2, there are two parties: the Radiant and the Dire.

    The Dota2 senate consists of senators coming from two parties. Now the senate wants to make a decision about a 
    change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can 
    exercise one of the two rights:

    Ban one senator's right:
    A senator can make another senator lose all his rights in this and all the following rounds.
    Announce the victory:
    If this senator found the senators who still have rights to vote are all from the same party, he can announce 
    the victory and make the decision about the change in the game.


    Given a string representing each senator's party belonging. The character 'R' and 'D' represent the Radiant 
    party and the Dire party respectively. Then if there are n senators, the size of the given string will be n.

    The round-based procedure starts from the first senator to the last senator in the given order. This procedure will 
    last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.

    Suppose every senator is smart enough and will play the best strategy for his own party, you need to predict 
    which party will finally announce the victory and make the change in the Dota2 game. The output should be Radiant or Dire.
"""

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        #iterate through the senate
        #if R increment the count, and append to the stack
        #only if count >= 0
        #if D decrease the count and append to the stack
        #only if count <= 0
        #one senate with same team
        
        queue = senate
        count = 0
        
        while queue:
            stack = []
            
            for i in queue:
                if i == 'R':
                    if count >= 0:
                        stack.append(i)
                    count += 1
                
                if i == 'D':
                    if count <= 0:
                        stack.append(i)
                    count -= 1
                
            queue = stack #append for round robin
            
            if len(set(stack)) == 1:
                if stack[0] == 'R':
                    return 'Radiant'
                
                return 'Dire'
