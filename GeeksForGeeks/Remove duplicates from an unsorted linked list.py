# User function Template for python3
'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None

'''


class Solution:
    # Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        # return head after editing list
        hashs = {}
        hashs[head.data] = 1
        temp = head
        while temp and temp.next:
            if temp.next.data in hashs:
                temp.next = temp.next.next
            else:
                hashs[temp.next.data] = 1
                temp = temp.next
        return head

