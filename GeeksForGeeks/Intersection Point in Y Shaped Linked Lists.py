# User function Template for python3
'''
	Function to return the value at point of intersection
	in two linked list, connected in y shaped form.

	Function Arguments: head_a, head_b (heads of both the lists)

	Return Type: value in NODE present at the point of intersection
	             or -1 if no common point.

	Contributed By: Nagendra Jha

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''


# Function to find intersection point in Y shaped Linked Lists.
def intersetPoint(head1, head2):
    # code here

    def length(node):
        s = node
        count = 0
        while s:
            s = s.next
            count += 1
        return count

    len1 = length(head1)
    len2 = length(head2)
    if len1 > len2:
        s = head2
        f = head1
    else:
        s = head1
        f = head2
    for i in range(abs(len2 - len1)):
        f = f.next
    while f and s:
        if f == s:
            return f.data
        f = f.next
        s = s.next
    return -1