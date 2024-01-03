# User function Template for python3

""" Node Class
    class Node:
        def __init__(self, data):   # data -> value stored in node
            self.data = data
            self.next = None
"""


class Solution:
    # Function to find first node if the linked list has a loop.
    def findFirstNode(self, head):
        # code here
        s = head
        f = head
        flag = 1
        while f != None and f.next != None:
            s = s.next
            f = f.next.next
            if s == f:
                flag = 0
                break
        if flag:
            return -1
        dummy = s.next
        count = 1
        while dummy != s:
            dummy = dummy.next
            count += 1

        s = head
        f = head
        for i in range(count):
            f = f.next
        while f != s:
            s = s.next
            f = f.next
        return s.data
