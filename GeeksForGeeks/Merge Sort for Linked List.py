# User function Template for python3

'''
    :param head: head of unsorted linked list
    :return: head of sorted linkd list

    # Node Class
    class Node:
        def __init__(self, data):  # data -> value stored in node
            self.data = data
            self.next = None
'''


class Solution:
    # Function to sort the given linked list using Merge Sort.
    def getMiddle(self, node):
        s = node
        f = node.next
        while f and f.next:
            s = s.next
            f = f.next.next
        return s

    def mergeSort(self, head):
        if head == None or head.next == None:
            return head
        left = head
        right = self.getMiddle(head)
        temp = right.next
        right.next = None
        right = temp
        left = self.mergeSort(left)
        right = self.mergeSort(right)
        return self.merge(left, right)

    def merge(self, left, right):
        dummy = Node(0)
        temp = dummy
        while left and right:
            if left.data < right.data:
                temp.next = left
                left = left.next
            else:
                temp.next = right
                right = right.next
            temp = temp.next
        if left:
            temp.next = left
        if right:
            temp.next = right
        return dummy.next
