"""
    Deep Copy of the Linked List with Random Pointers
"""
class Node():
    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None

class Solution():

    def printTraverse(self, head):
        while head:
            print(head.val, head.random.val if head.random != None else None)
            head = head.next

    def firstApproach(self, head):
        if head is None:
            return head

        #step 1 copied inbetween
        first = head
        while(head != None):
            temp = Node(head.next)
            next_node = head.next
            head.next = temp
            temp.next = next_node
            head.next = next_node
        
        head = first

        #step  2 connect with random pointers
        while(head != None):
            head.next.random = head.random.next if head.random != None else None
            head = head.next.next if head.next != None else head.next
        
        #step 3 separate original and random pointers
        orig = first
        copy = first.next
        result = copy
        
        while(orig != None and copy != None):
            orig.next = orig.next.next if orig.next != None else orig.next
            copy.next = copy.next.next if copy.next != None else copy.next
        
            #update the pointers
            orig = orig.next
            copy = copy.next
        
        return result
    
    def usingHashmap(self, head):
        if head is None:
            return head
        
        hashmap = {}
        firstNode = head
        secondNode, secondNext = None, None

        while head != None:
            newnode = Node(head.next)
            if secondNode is None:
                secondNext = newnode
                secondNode = secondNext
            else:
                secondNode.next = newnode
                secondNode = newnode

            hashmap[firstNode] = secondNext
            firstNode = firstNode.next
        
        print(hashmap)

        firstNode = head
        secondNode = secondNext

        while(firstNode):
            if firstNode.random is not None:
                secondNode.random = hashmap[firstNode.random]
            
            firstNode = firstNode.next
            secondNode = secondNode.next

        return secondNext
