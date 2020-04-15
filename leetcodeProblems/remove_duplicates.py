"""
    Problem Statement:
        Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only 
        distinct numbers from the original list.
        Return the linked list sorted as well.
"""

class Node():
    def __init__(self, val):
        self.value =val
        self.next = None

class Solution():

    def printList(self, node):
        while(node):
            print(node.value)
            node = node.next


    def remove_duplicates(self, root):
        hashmap = {}
        result = Node(0)
        curr = result

        while root:
            if root.value not in hashmap:
                hashmap[root.value] = 1
            else:
                hashmap[root.value] += 1
            
            root = root.next
        
        for k, v in hashmap.items():
            if v > 1:
                pass
            else:
                nn = Node(k)
                curr.next = nn
                curr = nn
        
        self.printList(result.next)

n1 = Node(1)
n2 = Node(1)
n3 = Node(1)
n4 = Node(2)
n5 = Node(2)
n6 = Node(3)

root = n1
root.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

n1 = Node(1)
n1.next = Node(2)
n1.next.next = Node(3)
n1.next.next.next = Node(3)
n1.next.next.next.next = Node(4)
n1.next.next.next.next = Node(4)
n1.next.next.next.next.next = Node(5)


print(Solution().remove_duplicates(root))
print(Solution().remove_duplicates(n1))