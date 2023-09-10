# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        count1 = self.findlength(headA)
        count2 = self.findlength(headB)
        a = headA
        b = headB
        if count1 > count2:
            for i in range(count1 - count2):
                a = a.next
        else:
            for i in range(count2 - count1):
                b = b.next
        while a != None and b != None:
            if a == b:
                return a
            a = a.next
            b = b.next
        return None

    def findlength(self, node):
        count = 0
        while node != None:
            count += 1
            node = node.next
        return count
