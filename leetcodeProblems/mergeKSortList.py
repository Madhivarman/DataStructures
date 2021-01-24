"""
    Problem Statement:
        Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""
class Node():
    def __init__(self, val):
        self.data = val
        self.next = None
    
class Solution:
    def mergeKLists(self, linkedListInList: List[ListNode]) -> ListNode:
            
            #instead of traversing throughe each element
            #we can simply use Dictionary
            head = ListNode(0)
            temp = head
            result = []
            
            if len(linkedListInList) == 0:
                return head.next
            
            for ll in linkedListInList:
                n = ll
                while n:
                    result.append(n.val)
                    n = n.next
            
            st = sorted(result)
            
            #print(st)
            
            for r in st:
                temp.next = ListNode(r)
                temp = temp.next
            
            return head.next


"""
[
  1->4->5,
  1->3->4,
  2->6
]
"""

if __name__ == "__main__":
    #node
    l1 = Node(1)
    l1_2 = Node(4)
    l1_3 = Node(5)

    l2 = Node(1)
    l2_2 = Node(3)
    l2_3 = Node(4)

    l3 = Node(2)
    l3_2 = Node(6)

    #connect the linked list
    l1.next = l1_2
    l1_2.next = l1_3

    l2.next = l2_2
    l2_2.next = l2_3

    l3.next = l3_2

    #connect on linkedList
    asList = [l1, l2, l3]
    solution = Solution().mergeKSortedLinkedList(asList)

    printLinkedList(solution)
