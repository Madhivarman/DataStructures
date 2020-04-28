
class Node():
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution():

    def printList(self, root):
        while(root):
            print(root.val)
            root = root.next

    def reverseList(self,head):

        prev = Node(None) #created an Empty Node
        curr = head # The Head Node is now current(curr) node

        while curr!= None: #Iterate until the Node is None
            nexttemp =  curr.next #created a temp Node to remember the next Node
            curr.next = prev # assigning the next Node of current as Prev (for first iteration it will be None)
            prev = curr # Now the prev become current
            curr = nexttemp # current become the node which we stored in the temp Node(nexttemp)
        
        self.printList(prev)
        return prev


#create node and connect nodes
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

root = n1
root.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

print(Solution().reverseList(root))
