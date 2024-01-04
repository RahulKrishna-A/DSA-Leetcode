# User function Template for python3
'''
	Your task is to segregate the list of
	0s,1s and 2s.

	Function Arguments: head of the original list.
	Return Type: head of the new list formed.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''


class Solution:
    # Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        # code here
        oneHead = Node(-1)
        zeroHead = Node(-1)
        twoHead = Node(-1)
        one = oneHead
        zero = zeroHead
        two = twoHead

        temp = head
        while temp:
            if temp.data == 0:
                zero.next = temp
                temp = temp.next
                zero = zero.next
                zero.next = None
            elif temp.data == 1:
                one.next = temp
                temp = temp.next
                one = one.next
                one.next = None
            else:
                two.next = temp
                temp = temp.next
                two = two.next

        two.next = None
        one.next = twoHead.next
        zero.next = oneHead.next

        return zeroHead.next