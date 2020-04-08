class Node():
    def __init__(self, val):
        self.val = val
        self.next = None
        
class Solution():

    def printList(self, nodes):
        while(nodes):
            print(nodes.val)
            nodes = nodes.next

    def removeDuplicates(self, root):
        final = temp = root
        if not root:
            return root
        
        while(temp.next):
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        
        self.printList(final)

root = Node(1)
n2 = Node(1)
n3 = Node(1)
n4 = Node(2)
n5 = Node(2)
n6 = Node(3)

root.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

print(Solution().removeDuplicates(root))