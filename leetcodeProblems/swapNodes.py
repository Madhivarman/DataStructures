"""
    Swap Nodes:
        Given a linked list, swap every two adjacent nodes and return its head.
        You may not modify the values in the list's nodes, only nodes itself may be changed.
"""
class Node():
    def __init__(self, val):
        self.data = val  
        self.next = None

def printLinkedList(ll):
    ans  = []
    temp = ll
    while temp:
        ans.append(temp.data)
        temp = temp.next
    
    print(ans)

def swapNodes(head):
    output = Node(0)
    
    if head==None or head.next == None:
        return head

    node = output
    while head and head.next:
        node.next = head.next # 0->2, 0->2->1->4
        node = node.next #pointer @ 2, pointer @4
        head.next = head.next.next # 1->3, 3 -> None
        node.next = head # 0 -> 2 -> 1, 0->2->1->4->3
        node = node.next # pointer @ 1, pointer @3
        head = head.next # head @ 3, head @ None
        node.next = head # 1->3, 3 -> None
    return output.next

if __name__ == "__main__":
    
    #create all the nodes
    root = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    #n5 = Node(5)

    #create a connection
    root.next = n2
    n2.next = n3
    n3.next = n4
    #n4.next = n5

    solution = swapNodes(root)


    #print the linked list to solve the problem
    printLinkedList(solution)