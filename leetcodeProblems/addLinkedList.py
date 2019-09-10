class Node:

	def __init__(self, val, next=()):
		self.data = val
		self.next = next


class LinkedList:

	def __init__(self):
		self.head = None


def ppresultList(ll):
	temp = ll

	while(temp):
		print(temp.data)
		temp = temp.next

def addTwoNumber(l1, l2):
	
	l1_temp, l2_temp = l1.head, l2.head
	sum_per_digit = [] #list to store sum per digit
	carry = 0

	while(l1_temp):
		current_sum = l1_temp.data + l2_temp.data + carry
		#bring the next node
		if len(str(current_sum)) == 1:
			sum_per_digit.append(current_sum)
		else:
			addup = int(list(str(current_sum))[1])
			sum_per_digit.append(addup)
			carry = int(list(str(current_sum))[0])


		l1_temp, l2_temp = l1_temp.next, l2_temp.next

	#return type should be in LinkedList
	resultLL = LinkedList()
	resultLL.head = Node(sum_per_digit[0])

	resultLL_copy = resultLL

	#iterate through the list
	def listToLinkedList(lst):
		assert len(lst) > 0
		if len(lst) == 1:
			rrl = Node(lst[0])
			return rrl
		else:
			rrl = Node(lst[0], listToLinkedList(lst[1:]))
			return rrl

	a = listToLinkedList(sum_per_digit)
	ppresultList(a)

if __name__ == '__main__':

	# (2 -> 4 -> 3) + (5 -> 6 -> 4)
	#  7 -> 0 -> 8 

	#constraints should carry remainder to the next node
	l1_First = Node(2)
	l1_second = Node(4)
	l1_third = Node(3)

	l2_First = Node(5)
	l2_second = Node(6)
	l2_third = Node(4)

	l1 = LinkedList()
	l1.head = l1_First
	l1.head.next = l1_second
	l1_second.next = l1_third

	l2 = LinkedList()
	l2.head = l2_First
	l2.head.next = l2_second
	l2_second.next = l2_third

	addTwoNumber(l1, l2)