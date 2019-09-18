"""
    Problem Statement:
        Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""
class Node():
    def __init__(self, val):
        self.data = val
        self.next = None
    
def printLinkedList(ll):
    temp = ll
    ans = []
    while temp:
        ans.append(temp.data)
        temp = temp.next
    
    print(ans)
        

def mergeKSortedLinkedList(linkedListInList):
    #instead of traversing throughe each element
    #we can simply use Dictionary
    head = Node(0)
    temp = head
    dictionary = dict()

    if len(linkedListInList) == 0:
        return head.next
    
    #iterate through the dictionary keys
    for node in linkedListInList:
        while node:
            if node.data not in dictionary:
                dictionary[node.data] = [node]
            else:
                dictionary[node.data].append(node)
            #update the node
            node = node.next
    
    keys = list(dictionary.keys())
    keys = sorted(keys) #sorted the keys

    for key in keys:
        for node in dictionary.get(key):
            temp.next = node
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
    solution = mergeKSortedLinkedList(asList)

    printLinkedList(solution)