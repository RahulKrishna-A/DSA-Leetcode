# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None:
            return
        first = head
        mid = self.middle(head)
        secondpart = self.reverse(mid)
        while first != None and secondpart != None:
            temp = first.next
            first.next = secondpart
            first = temp
            temp2 = secondpart.next
            secondpart.next = first
            secondpart = temp2
        if first != None:
            first.next = None

    def middle(self, head):
        slow = head
        fast = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse(self, head):
        if head == None:
            return head
        prev = None
        pres = head
        Next = head.next
        while pres != None:
            pres.next = prev
            prev = pres
            pres = Next
            if Next != None:
                Next = Next.next
        return prev
