"""
    Given a linked list, remove the n-th node from the end of list and return its head.
"""
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
    


def printNodeList(asList):
    temp = asList[0] #root node
    l = []
    while(temp != None):
        l.append(temp.data)
        temp = temp.next

    print(l)

#function to get the nth node from linked list
def getNthNodeFromLinkedList(rootNode, k):
    #get the length of the linked list
    N = 1
    temp = rootNode

    #get the nth Node
    while(temp.next != None):
        N += 1
        temp =  temp.next
    
    #Index of the node to remove
    nthElement = N - k
    indexStart = 1 #start position

    previousNode = rootNode
    currentNode = rootNode
    addingNode = []
    addingNode.append(previousNode)

    while(indexStart < N):
        #update the current node as previous node
        previousNode = currentNode
        currentNode = currentNode.next

        addingNode.append(currentNode)
        
        #if condition mets then break
        if indexStart == nthElement:
            previousNode.next = currentNode.next

        indexStart += 1

    printNodeList(addingNode)

k = 5 #Kth Number

root = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

#appending each node to its end
root.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

ss = getNthNodeFromLinkedList(root, k)



