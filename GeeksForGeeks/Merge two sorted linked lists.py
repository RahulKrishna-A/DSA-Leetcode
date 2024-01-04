# User function Template for python3
'''
	Function to merge two sorted lists in one
	using constant space.

	Function Arguments: head_a and head_b (head reference of both the sorted lists)
	Return Type: head of the obtained list after merger.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''


# Function to merge two sorted linked list.
def sortedMerge(head1, head2):
    # code here
    dummy = Node(0)
    temp = dummy
    ll1 = head1
    ll2 = head2
    while ll1 != None and ll2 != None:
        if ll1.data > ll2.data:
            temp.next = ll2
            temp = temp.next
            ll2 = ll2.next
        else:
            temp.next = ll1
            temp = temp.next
            ll1 = ll1.next
    if ll1 != None:
        temp.next = ll1
    if ll2 != None:
        temp.next = ll2
    return dummy.next