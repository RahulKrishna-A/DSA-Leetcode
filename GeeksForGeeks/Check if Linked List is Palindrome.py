# User function Template for python3
'''
	Your task is to check if given linkedlist
	is a pallindrome or not.

	Function Arguments: head (reference to head of the linked list)
	Return Type: boolean , no need to print just return True or False.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

	Contributed By: Nagendra Jha
'''


# Function to check whether the list is palindrome.
class Solution:
    def isPalindrome(self, head):
        # code here
        if head == None or head.next == None:
            return True
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        slow = self.reverse(slow)

        # slow = slow.next
        dummy = head
        while slow != None:
            if dummy.data != slow.data:
                return 0
            dummy = dummy.next
            slow = slow.next
        return True

    def reverse(self, node):
        if node == None:
            return None
        prev = None
        pres = node
        next = node.next
        while pres:
            pres.next = prev
            prev = pres
            pres = next
            if next:
                next = next.next
        return prev

