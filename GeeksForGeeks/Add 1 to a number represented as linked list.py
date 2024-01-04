# User function Template for python3

'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''


class Solution:

    def reverseLL(self, node):
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

    def addOne(self, head):
        # Returns new head of linked List.

        rvhead = self.reverseLL(head)
        temp = rvhead
        carry = 1
        while temp:
            val = temp.data + carry
            temp.data = val % 10
            carry = val // 10
            temp = temp.next
        nwhead = self.reverseLL(rvhead)
        if carry:
            new_node = Node(1)
            new_node.next = nwhead
            return new_node
        return nwhead


