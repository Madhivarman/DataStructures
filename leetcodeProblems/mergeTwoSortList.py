"""
    Problem Statement:
        Merge two sorted linked lists and return it as a new list. The new 
        list should be made by splicing together the nodes of the first two
        lists.
"""
class Node():
    def __init__(self, val):
        self.data = val
        self.next = None

def printLinkedList(ll):
    temp = ll
    values = []
    while(temp.next != None):
        values.append(temp.data)
        temp = temp.next
    
    print(values)

def mergeTwoSortList(list1, list2=None):
    #create a new node
    head = Node(0)
    new_list = head

    while True:
        if list2 is None:
            new_list.next = list1
            break
        elif list1 is None:
            new_list.next = list2
            break

        if list1.data <= list2.data:
            new_list.next = list1
            new_list = new_list.next
            list1 = list1.next
        
        elif list1.data > list2.data:
            new_list.next = list2
            new_list = new_list.next
            list2 = list2.next
        

    return head.next

if __name__ == "__main__":
    l1 = Node(1)
    l1_2 = Node(2)
    l1_3 = Node(3)

    #l2 = Node(None)

    """
    l2 = Node(1)
    l2_2 = Node(3)
    l2_3 = Node(4)
    """
    #create a linked list
    l1.next = l1_2
    l1_2.next = l1_3

    """
    l2.next = l2_2
    l2_2.next = l2_3
    """

    s = mergeTwoSortList(l1)
    print(s)