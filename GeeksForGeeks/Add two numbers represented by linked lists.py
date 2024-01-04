# User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


class Solution:
    # Function to add two numbers represented by linked list.
    def reversedLL(self, node):
        prev = None
        pres = node
        next = pres.next
        while pres:
            pres.next = prev
            prev = pres
            pres = next
            if next:
                next = next.next
        return prev

    def addTwoLists(self, first, second):
        # code here
        # return head of sum list
        rvfirst = self.reversedLL(first)
        rvsecond = self.reversedLL(second)
        dummy = Node(0)
        temp = dummy
        car = 0
        while rvfirst or rvsecond or car:
            v1 = rvfirst.data if rvfirst else 0
            v2 = rvsecond.data if rvsecond else 0
            if rvfirst:
                rvfirst = rvfirst.next
            if rvsecond:
                rvsecond = rvsecond.next
            sums = v1 + v2 + car
            car = sums // 10
            sums = sums % 10
            dummy.next = Node(sums)
            dummy = dummy.next
        return self.reversedLL(temp.next)
