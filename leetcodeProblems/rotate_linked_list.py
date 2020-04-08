"""
    Problem Statement:
        Given a linked list, rotate the list to the right by k places, where k is non-negative.
        Input: 1->2->3->4->5->NULL, k = 2
        Output: 4->5->1->2->3->NULL
        Explanation:
        rotate 1 steps to the right: 5->1->2->3->4->NULL
        rotate 2 steps to the right: 4->5->1->2->3->NULL
"""

class Node():
    def __init__(self, val):
        self.node = val
        self.next = None

class Solution():

    def printList(self, nodes, verbose=False):
        count = 0
        while(nodes):
            if verbose:
                print(nodes.node)

            nodes = nodes.next
            count += 1
        
        return count
    
    def rotateonce(self, root):
        head = root
        pp, np = root, root.next
        
        while(np.next != None):
            pp = np
            np = np.next
        
        pp.next = None
        np.next = head

        head = np

        return head

    def rotateRight(self, head, K):
        count = self.printList(head)
        K = K % count

        #rotate K times
        for i in range(K):
            head = self.rotateonce(head)
        
        self.printList(head, verbose=True)



#creat a list
"""root = Node(1)
v2 = Node(2)
v3 = Node(3)
v4 = Node(4)
v5 = Node(5)

root.next = v2
v2.next = v3
v3.next = v4
v4.next = v5"""

root = Node(1)
v2 = Node(2)
v3 = Node(3)

root.next = v2
v2.next = v3

#print(Solution().rotateRight(root, 2))
print(Solution().rotateRight(root, 2000000000))