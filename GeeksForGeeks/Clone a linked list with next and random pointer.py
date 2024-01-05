# User function Template for python3

'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.arb=None

param: head:  head of linkedList to copy
return: the head of the copied linked list the #output will be 1 if successfully copied
'''


class Solution:
    # Function to clone a linked list with next and random pointer.
    def copyList(self, head):
        # code here
        if head == None:
            return head
        temp = head
        while temp:
            newnode = Node(temp.data)
            newnode.next = temp.next
            temp.next = newnode
            temp = temp.next.next
        temp = head
        while temp:
            if temp.arb:
                temp.next.arb = temp.arb.next
            temp = temp.next.next

        cur = head
        clonedhead = cur.next
        clonedcurr = clonedhead

        while clonedcurr.next:
            cur.next = cur.next.next
            clonedcurr.next = clonedcurr.next.next
            cur = cur.next
            clonedcurr = clonedcurr.next
        cur.next = None
        clonedcurr.next = None
        return clonedhead