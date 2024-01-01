# function Template for python3

"""
# Node Class

class node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""


class Solution:
    # Function to reverse a linked list.
    def reverseList(self, head):
        # Code here
        prev = None
        pres = head
        next = head.next
        while pres:
            pres.next = prev
            prev = pres
            pres = next
            if next:
                next = next.next
        return prev
