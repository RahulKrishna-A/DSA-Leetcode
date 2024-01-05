# User function Template for python3

'''
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

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

    def compute(self, head):
        # Your code here
        reversedLL = self.reverseLL(head)
        temp = reversedLL
        while temp and temp.next:
            if temp.data > temp.next.data:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return self.reverseLL(reversedLL)
