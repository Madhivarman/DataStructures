"""
Given a linked list, reverse the nodes of a linked list k at a time and
return its modified list.
k is a positive integer and is less than or equal to the length of the
linked list. If the number of nodes is not a multiple of k then left-out 
nodes in the end should remain as it is.
"""
class Node():
    def __init__(self, val):
        self.data = val  
        self.next = None

def printKNodes(ll):
    arr = []
    while ll:
        arr.append(ll.data)
        ll = ll.next
    
    return arr


def reverseNodes(head):
    prev = None
    curr = head
    nextnode = None

    while(curr != None):
        nextnode = curr.next # update the next node 
        curr.next = prev #make previous node as next for current node
        prev = curr #update the current nodes as previous node 
        curr = nextnode #update next node as current node
    
    return prev


def reverseKNodes(copy, kgroup):
    #get the remaining nodes;
    def get_remaining_nodes(nodes, kn):
        start = nodes
        tmp = nodes
        try:
            for _ in range(0, k-1):
                tmp = tmp.next
            return tmp
        except:
            return start
        
    remainingNodes = get_remaining_nodes(copy, kgroup)
    s = printKNodes(remainingNodes)
    print(s)

if __name__ == "__main__":
    
    #create all the nodes
    root = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)

    #create a connection
    root.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    k = 2

    solution = reverseKNodes(root, k)
    #print(printKNodes(solution))