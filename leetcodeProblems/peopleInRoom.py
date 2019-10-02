"""
    Problem Statement:
        Given two  lists L1 and L2. L1 has starting time, L2 has ending time. 
        Both lists represents time in minutes. With given K=2 minutes, you need to tell
        how many people are there in the room at given minutes.
    
    Example:
        For example,
            L1 = [1,1,1,2,2,3,3,4,4,4,5,5,5,6,7]
            L2 = [2,3,4,4,5,5,6,6,6,6,7,7,7,8,9]
            K = 6
        
        Output: 4 
    
    ie..., 4 People are there in that moment
"""
def findPeople(startTime, endTime, mins):
    peopleInRoom = 0

    #return zero, if no incomings and outgoings
    if len(startTime) == 0 and len(endTime) == 0:
        return peopleInRoom
    
    #people who all coming into the room
    #stays in the room
    if len(endTime) == 0:
        return len(startTime)
    
    ziplist = zip(startTime, endTime)

    for room_in, room_out in ziplist:
        if room_in < mins and room_out > mins:
            peopleInRoom += 1 

    return peopleInRoom

incoming = [1,1,1,2,2,3,3,4,4,4,5,5,5,6,7]
outgoing = [2,9,4,4,5,5,6,6,6,6,7,7,7,8,9]

incoming_1 = [1,1,3,3,3,5,6,6]
outgoing_1 = [6,3,5,6,2,8,9,7]
mins = 5
mins_2 = 6
n = findPeople(incoming, outgoing, mins)
n_2 = findPeople(incoming_1, outgoing_1, mins_2)
print("with given minute, current number of people in room are:{}".format(n))
