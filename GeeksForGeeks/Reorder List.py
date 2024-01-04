# User function Template for python3

# User function Template for python3

# Node Class
class node:
    def __init__(self, val):
        self.data = val
        self.next = None


# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None


# Back-end complete function Template for Python 3
class Solution:

    def reverse(self, node):
        prev = None
        pres = node
        if node == None:
            return None
        next = node.next
        while pres:
            pres.next = prev
            prev = pres
            pres = next
            if next:
                next = next.next
        return prev

    def reorderList(self, head):
        s = head
        f = head.next
        if head == None and head.next == None and head.next.next == None:
            return head
        while f and f.next:
            s = s.next
            f = f.next.next
        ll1 = head
        ll2 = s.next
        s.next = None
        ll2 = self.reverse(ll2)

        nodes = node(0)
        temp = nodes
        while ll1 or ll2:
            if ll1 != None:
                temp.next = ll1
                ll1 = ll1.next
                temp = temp.next
            if ll2 != None:
                temp.next = ll2
                ll2 = ll2.next
                temp = temp.next
        return nodes.next
